#include <windows.h>
#include <stdio.h>
#include <signal.h>

LRESULT CALLBACK LowLevelKeyboardProc(int nCode, WPARAM wParam, LPARAM lParam);
void sigintHandler(int sig_num);

int main(int argc, char *argv[])
{
    fprintf(stderr, "Logging keys. Ctrl+C to exit.\n");
    signal(SIGINT, sigintHandler);

    HINSTANCE app = GetModuleHandle(NULL);
    SetWindowsHookEx(WH_KEYBOARD_LL, LowLevelKeyboardProc, app, 0);

    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0) > 0) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    fflush(stdout);
    return 0;
}

LRESULT CALLBACK LowLevelKeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
  KBDLLHOOKSTRUCT *kb=(KBDLLHOOKSTRUCT *)lParam;
  if (wParam == WM_KEYDOWN) {
    fprintf(stdout, "down %i\n", kb->vkCode);
  } else if (wParam == WM_KEYUP) {
    fprintf(stdout, "up %i\n", kb->vkCode);
  } else if (wParam == WM_SYSKEYDOWN) {
    fprintf(stdout, "down %i\n", kb->vkCode);
  } else if (wParam == WM_SYSKEYUP) {
    fprintf(stdout, "up %i\n", kb->vkCode);
  } else {
    fprintf(stdout, "Unknown keyboard event\n");
  }
  return 0;
}

void sigintHandler(int sig_num) {
  fflush(stdout);
  exit(0);
}