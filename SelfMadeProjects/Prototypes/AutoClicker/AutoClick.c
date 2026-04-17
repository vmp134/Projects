#include "AutoClick.h"

//Main
/*
 * This will serve as an autoclicker for my current OS, Fedora KDE
 * Our program will take at most two arguments: <ms_delay> and <button_code>
 * If <button_code> is not supplied, default to left click
 */
int main(int argc, char *argv[]) {
    //Guard Clause
    if (argc > 3 || argc == 1) {
        printf("Error: Incorrect # of arguments\nUsage: %s <delay_ms> <button_code>\nUsage: %s <delay_ms>", argv[0]);
        return EXIT_FAILURE;
    }

    //Argument handling
    int delay = atoi(argv[1]);
    int button_type = atoi(argv[2]);

    if (delay <= 0) {
        printf ("Error: Incorrect argument, <ms_delay> must be a nonzero positive number");
        return EXIT_FAILURE;
    }
    int button = BTN_LEFT;
    if (argc == 3) {
        if (button_type == 1) 
            button = BTN_MIDDLE;
        else if (button_type == 2) 
            button = BTN_RIGHT;
        else if (button_type != 0) {
            printf("Error: Incorrect argument, <button_code> accepts:\n0: Left Click\n1: Middle Click\n2:Right Click");
            return EXIT_FAILURE;
        }
    }

    //Setup, with an FD to /dev/uinput and our uinput_setup struct
    int fd = open("/dev/uinput", O_WRONLY | O_NONBLOCK);
    struct uinput_setup usetup;

    //Configuring mouse clicks
    ioctl(fd, UI_SET_EVBIT, EV_KEY); 
    ioctl(fd, UI_SET_KEYBIT, button);

    //Click
    while(1) {
        
    }

    //Cleanup
    
    close(fd);
    return EXIT_SUCCESS;
}