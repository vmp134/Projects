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
        printf("Error: Incorrect # of arguments\nUsage: %s <delay_ms> <button_code>\nUsage: %s <delay_ms>", argv[0], argv[0]);
        return EXIT_FAILURE;
    }

    //Argument handling
    int delay = atoi(argv[1]);

    if (delay <= 0) {
        printf ("Error: Incorrect argument, <ms_delay> must be a nonzero positive number");
        return EXIT_FAILURE;
    }
    int button = BTN_LEFT;
    if (argc == 3) {
        int button_type = atoi(argv[2]);
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
    memset(&usetup, 0, sizeof(usetup));
    usetup.id.bustype = BUS_USB;
    usetup.id.vendor  = 0x1234;
    usetup.id.product = 0x5678; 
    strcpy(usetup.name, "Gemini-Autoclicker");

    struct input_event ev_syn;
    memset(&ev_syn, 0, sizeof(ev_syn));
    ev_syn.type = EV_SYN;
    ev_syn.code = SYN_REPORT;
    ev_syn.value = 0;

    struct input_event ev_press; 
    memset(&ev_press, 0, sizeof(ev_press));
    ev_press.type = EV_KEY;
    ev_press.code = button;
    ev_press.value = 1; // 1 for Press

    struct input_event ev_rel;
    memset(&ev_rel, 0, sizeof(ev_rel));
    ev_rel.type = EV_KEY;
    ev_rel.code = button;
    ev_rel.value = 0; // 0 for Release


    //Configuring mouse clicks
    int ev = ioctl(fd, UI_SET_EVBIT, EV_KEY); 
    int key = ioctl(fd, UI_SET_KEYBIT, button);
    if (ev < 0 || key < 0) {
        perror("ioctl");
        return EXIT_FAILURE;
    }

    if (ioctl(fd, UI_DEV_SETUP, &usetup) < 0) {
        perror("UI_DEV_SETUP");
        return EXIT_FAILURE;
    }

    if (ioctl(fd, UI_DEV_CREATE) < 0) {
        perror("UI_DEV_CREATE");
        return EXIT_FAILURE;
    }

    //Click
    while(1) {
        write(fd, &ev_press, sizeof(ev_press));
        write(fd, &ev_syn, sizeof(ev_syn));

        write(fd, &ev_rel, sizeof(ev_rel));
        write(fd, &ev_syn, sizeof(ev_syn));

        usleep(delay * 1000); 
    }

    //Cleanup
    ioctl(fd, UI_DEV_DESTROY);    
    close(fd);
    return EXIT_SUCCESS;
}