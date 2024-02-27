#include <io.h>
#include <stdio.h>
#include <Shlobj.h>
#include <Windows.h>

#define MAX_PATH_LENGTH 512


wchar_t* char2wchar(const char* cchar, size_t m_encode = CP_ACP)
{
    wchar_t* m_wchar;
    int len = MultiByteToWideChar(m_encode, 0, cchar, strlen(cchar), NULL, 0);
    m_wchar = new wchar_t[len + 1];
    MultiByteToWideChar(m_encode, 0, cchar, strlen(cchar), m_wchar, len);
    m_wchar[len] = '\0';
    return m_wchar;
}


int main(int argc, char** argv)
{
    ITEMIDLIST* dir = NULL;    //Directory to open
    ITEMIDLIST** _selection = NULL;
    LPCITEMIDLIST* selection = NULL;    //Items in directory to select
    WIN32_FIND_DATAW FindFileData;
    char path[MAX_PATH_LENGTH] = { 0 };
    int count, ret = 0;

    if (argc <= 1) {
        printf("A simple file selector.\nUsage:\n  select {Location} [Item1 [Item2 [Item3 ...]]]\n  \
If providing Item, select given items in directory Location,\notherwise select Location only.\n");
        goto end;
    }

    // Allocate buffer
    _selection = (ITEMIDLIST**)calloc(argc, sizeof(ITEMIDLIST*));
    selection = (LPCITEMIDLIST*)calloc(argc, sizeof(LPCITEMIDLIST));
    if (!(_selection && selection)) {
        printf("Error: Fail to allocate memory.\n");
        ret = -1;  goto end;
    }

    // Parse argument
    if (argc == 2) {
        if (!_access(argv[1], 0)) {
            count = 1;
            strncpy_s(path, MAX_PATH_LENGTH, argv[1], strlen(argv[1]) - strlen(strrchr(argv[1], '\\')));
            dir = ILCreateFromPath(char2wchar(path));
            _selection[0] = ILCreateFromPath(char2wchar(argv[1]));
            selection[0] = _selection[0];
        }
        else {
            printf("Error: File or directory '%s' doesn't exist.", argv[1]);
            ret = -2; goto end;
        }
    }
    else {
        FindFirstFile(char2wchar(argv[1]), &FindFileData);
        if (FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
        {
            count = argc - 2;
            dir = ILCreateFromPath(char2wchar(argv[1]));
            for (int i = 0; i < count; i++) {
                snprintf(path, MAX_PATH_LENGTH, "%s\\%s", argv[1], argv[i + 2]);
                if (!_access(path, 0)) {
                    _selection[i] = ILCreateFromPath(char2wchar(path));
                    selection[i] = _selection[i];
                }
                else {
                    printf("Error: Item '%s' doesn't exist.\n", path);
                    ret = -3; goto end;
                }
            }
        }
        else
        {
            printf("Error: '%s' isn't an existing directory.", argv[1]);
            ret = -2;  goto end;
        }
    }
    
    //Perform selection
    if (CoInitializeEx(NULL, COINIT_MULTITHREADED) != 0) {
        printf("Error: Fail to initialize COM library.\n");
        ret = -4;  goto end;
    }
    SHOpenFolderAndSelectItems(dir, (UINT)count, selection, 0);

end:
    //Free resources
    if (dir)
        ILFree(dir);
    if (selection)
        free(selection);
    if (_selection) {
        for (int i = 0; i < argc; i++)
            ILFree(_selection[i]);
        free(_selection);
    }

    return ret;
}