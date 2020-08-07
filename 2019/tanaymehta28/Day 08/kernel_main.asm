BITS 32

start:
    mov ax, 07C0h   ;4K Stack Space
    add ax, 288     ;16 Bytes Per Paragraph
    mov ax, ss 
    mov 4096, sp
    mov ax, 07C0h
    mov ds, ax    

    mov si, text_string 
    call print_string

    jmp $

    text_string db 'Welcome to Project DarkSpark v0.1. We are happy to have you Test our OS', 0

print_string:
    mov ah, 0Eh

.repeat:
    lodsb
    cmp al, 0
    je .done
    int 10h
    jmp .repeat

.done:
    ret
    times 510-($-$$) db 0

    dw 0xAA55
