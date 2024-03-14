from tkinter import *
from turtle import clear
import customtkinter
from PIL import Image, ImageTk


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


def change_img(thisImage_label, new_image):
    thisImage_label.config(image=new_image)
    thisImage_label.image = new_image


def change_text(text_label, txt):
    text_label.config(text=txt)

# identifies which valves should be closed
def which_valves(parval, serval, setval, orgval):
    if setval == '1' or setval == '':
        if parval == '0' or parval == '':
            if serval == '2':
                if orgval == 'AB' or orgval == 'ab' or orgval == '':
                    p0s2op1 = PhotoImage(file='pics2/p0s2op1.png')
                    change_img(image_label, p0s2op1)
                    change_text(valvesOutput, "5, 6, 7")
                    change_text(serialOutput, "A, B")
                    change_text(paralOutput, "")
                    return
                if orgval == 'CD' or orgval == 'cd':
                    p0s2op2 = PhotoImage(file='pics2/p0s2op2.png')
                    change_img(image_label, p0s2op2)
                    change_text(valvesOutput, "5, 6, 7, 12, 13, 14")
                    change_text(serialOutput, "C, D")
                    change_text(paralOutput, "")
                    return
                if orgval == 'EF' or orgval == 'ef':
                    p0s2op3 = PhotoImage(file='pics2/p0s2op3.png')
                    change_img(image_label, p0s2op3)
                    change_text(valvesOutput, "12, 13, 14")
                    change_text(serialOutput, "E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'AC' or orgval == 'ac':
                    p0s2op4 = PhotoImage(file='pics2/p0s2op4.png')
                    change_img(image_label, p0s2op4)
                    change_text(valvesOutput, "3, 5, 10, 12, 13")
                    change_text(serialOutput, "A, C")
                    change_text(paralOutput, "")
                    return
                if orgval == 'CF' or orgval == 'cf':
                    p0s2op5 = PhotoImage(file='pics2/p0s2op5.png')
                    change_img(image_label, p0s2op5)
                    change_text(valvesOutput, "5, 6, 10, 12, 17")
                    change_text(serialOutput, "C, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BD' or orgval == 'bd':
                    p0s2op6 = PhotoImage(file='pics2/p0s2op6.png')
                    change_img(image_label, p0s2op6)
                    change_text(valvesOutput, "2, 7, 9, 13, 14")
                    change_text(serialOutput, "B, D")
                    change_text(paralOutput, "")
                    return
                if orgval == 'DF' or orgval == 'df':
                    p0s2op7 = PhotoImage(file='pics2/p0s2op7.png')
                    change_img(image_label, p0s2op7)
                    change_text(valvesOutput, "6, 7, 9, 14, 16")
                    change_text(serialOutput, "D, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'AD' or orgval == 'ad':
                    p0s2op8 = PhotoImage(file='pics2/p0s2op8.png')
                    change_img(image_label, p0s2op8)
                    change_text(valvesOutput, "3, 5, 7, 9, 13, 14")
                    change_text(serialOutput, "A, D")
                    change_text(paralOutput, "")
                    return
                if orgval == 'AF' or orgval == 'af':
                    p0s2op9 = PhotoImage(file='pics2/p0s2op9.png')
                    change_img(image_label, p0s2op9)
                    change_text(valvesOutput, "3, 5, 9, 10, 14, 16")
                    change_text(serialOutput, "A, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BC' or orgval == 'bc':
                    p0s2op10 = PhotoImage(file='pics2/p0s2op10.png')
                    change_img(image_label, p0s2op10)
                    change_text(valvesOutput, "2, 5, 7, 10, 12, 13")
                    change_text(serialOutput, "B, C")
                    change_text(paralOutput, "")
                    return
                if orgval == 'CF' or orgval == 'cf':
                    p0s2op11 = PhotoImage(file='pics2/p0s2op11.png')
                    change_img(image_label, p0s2op11)
                    change_text(valvesOutput, "5, 6, 10, 12, 14, 16")
                    change_text(serialOutput, "C, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'DE' or orgval == 'de':
                    p0s2op12 = PhotoImage(file='pics2/p0s2op12.png')
                    change_img(image_label, p0s2op12)
                    change_text(valvesOutput, "6, 7, 9, 12, 14, 17")
                    change_text(serialOutput, "D, E")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BE' or orgval == 'be':
                    p0s2op13 = PhotoImage(file='pics2/p0s2op13.png')
                    change_img(image_label, p0s2op13)
                    change_text(valvesOutput, "2, 7, 9, 10, 12, 17")
                    change_text(serialOutput, "B, E")
                    change_text(paralOutput, "")
                    return

            if serval == '3':
                if orgval == 'ABD' or orgval == 'abd' or orgval == '':
                    p0s3op1 = PhotoImage(file='pics2/p0s3op1.png')
                    change_img(image_label, p0s3op1)
                    change_text(valvesOutput, "5, 6, 9, 14, 16, 17")
                    change_text(serialOutput, "A, B, D")
                    change_text(paralOutput, "")
                    return
                if orgval == 'CDF' or orgval == 'cdf':
                    p0s3op2 = PhotoImage(file='pics2/p0s3op2.png')
                    change_img(image_label, p0s3op2)
                    change_text(valvesOutput, "5, 6, 7, 12, 13, 16")
                    change_text(serialOutput, "C, D, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BCD' or orgval == 'bcd':
                    p0s3op3 = PhotoImage(file='pics2/p0s3op3.png')
                    change_img(image_label, p0s3op3)
                    change_text(valvesOutput, "2, 5, 6, 12, 13, 14")
                    change_text(serialOutput, "B, C, D")
                    change_text(paralOutput, "")
                    return
                if orgval == 'DEF' or orgval == 'def':
                    p0s3op4 = PhotoImage(file='pics2/p0s3op4.png')
                    change_img(image_label, p0s3op4)
                    change_text(valvesOutput, "2, 3, 7, 9, 12, 13")
                    change_text(serialOutput, "D, E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABF' or orgval == 'abf':
                    p0s3op5 = PhotoImage(file='pics2/p0s3op5.png')
                    change_img(image_label, p0s3op5)
                    change_text(valvesOutput, "5, 6, 11, 13, 16")
                    change_text(serialOutput, "A, B, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BEF' or orgval == 'bef':
                    p0s3op6 = PhotoImage(file='pics2/p0s3op6.png')
                    change_img(image_label, p0s3op6)
                    change_text(valvesOutput, "2, 6, 11, 12, 13")
                    change_text(serialOutput, "B, E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABC' or orgval == 'abc':
                    p0s3op7 = PhotoImage(file='pics2/p0s3op7.png')
                    change_img(image_label, p0s3op7)
                    change_text(valvesOutput, "6, 7, 10, 12, 16, 17")
                    change_text(serialOutput, "A, B, C")
                    change_text(paralOutput, "")
                    return
                if orgval == 'CDE' or orgval == 'cde':
                    p0s3op8 = PhotoImage(file='pics2/p0s3op8.png')
                    change_img(image_label, p0s3op8)
                    change_text(valvesOutput, "5, 6, 7, 13, 14, 17")
                    change_text(serialOutput, "C, D, E")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ACD' or orgval == 'acd':
                    p0s3op9 = PhotoImage(file='pics2/p0s3op9.png')
                    change_img(image_label, p0s3op9)
                    change_text(valvesOutput, "3,6, 7, 12, 13, 14")
                    change_text(serialOutput, "A, C, D")
                    change_text(paralOutput, "")
                    return
                if orgval == 'CEF' or orgval == 'cef':
                    p0s3op10 = PhotoImage(file='pics2/p0s3op10.png')
                    change_img(image_label, p0s3op10)
                    change_text(valvesOutput, "2, 3, 5, 10, 13, 14")
                    change_text(serialOutput, "C, E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABE' or orgval == 'abe':
                    p0s3op11 = PhotoImage(file='pics2/p0s3op11.png')
                    change_img(image_label, p0s3op11)
                    change_text(valvesOutput, "6, 7, 8, 13, 17")
                    change_text(serialOutput, "A, B, E")
                    change_text(paralOutput, "")
                    return
                if orgval == 'AEF' or orgval == 'aef':
                    p0s3op12 = PhotoImage(file='pics2/p0s3op12.png')
                    change_img(image_label, p0s3op12)
                    change_text(valvesOutput, "3, 6, 8, 13, 14")
                    change_text(serialOutput, "A, E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ACF' or orgval == 'acf':
                    p0s3op13 = PhotoImage(file='pics2/p0s3op13.png')
                    change_img(image_label, p0s3op13)
                    change_text(valvesOutput, "3, 6, 10, 12, 14, 16")
                    change_text(serialOutput, "A, C, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BCE' or orgval == 'bce':
                    p0s3op14 = PhotoImage(file='pics2/p0s3op14.png')
                    change_img(image_label, p0s3op14)
                    change_text(valvesOutput, "2, 5, 7, 10, 13, 17")
                    change_text(serialOutput, "B, C, E")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BDE' or orgval == 'bde':
                    p0s3op15 = PhotoImage(file='pics2/p0s3op15.png')
                    change_img(image_label, p0s3op15)
                    change_text(valvesOutput, "2, 6, 9, 12, 14, 17")
                    change_text(serialOutput, "B, D, E")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ADF' or orgval == 'adf':
                    p0s3op16 = PhotoImage(file='pics2/p0s3op16.png')
                    change_img(image_label, p0s3op16)
                    change_text(valvesOutput, "3, 5, 7, 9, 13, 16")
                    change_text(serialOutput, "A, D, F")
                    change_text(paralOutput, "")
                    return

            if serval == '4':
                if orgval == 'ABCD' or orgval == 'abcd' or orgval == '':
                    p0s4op1 = PhotoImage(file='pics2/p0s4op1.png')
                    change_img(image_label, p0s4op1)
                    change_text(valvesOutput, "5, 6, 12, 13, 14")
                    change_text(serialOutput, "A, B, C, D")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABEF' or orgval == 'abef':
                    p0s4op2 = PhotoImage(file='pics2/p0s4op2.png')
                    change_img(image_label, p0s4op2)
                    change_text(valvesOutput, "5, 6, 11, 12, 13")
                    change_text(serialOutput, "A, B, E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'CDEF' or orgval == 'cdef':
                    p0s4op3 = PhotoImage(file='pics2/p0s4op3.png')
                    change_img(image_label, p0s4op3)
                    change_text(valvesOutput, "5, 6, 7, 12, 13")
                    change_text(serialOutput, "C, D, E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ACDF' or orgval == 'acdf':
                    p0s4op4 = PhotoImage(file='pics2/p0s4op4.png')
                    change_img(image_label, p0s4op4)
                    change_text(valvesOutput, "3, 6, 7, 12, 13, 16")
                    change_text(serialOutput, "A, C, D, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BCDE' or orgval == 'bcde':
                    p0s4op5 = PhotoImage(file='pics2/p0s4op5.png')
                    change_img(image_label, p0s4op5)
                    change_text(valvesOutput, "2, 5, 6, 13, 14, 17")
                    change_text(serialOutput, "B, C, D, E")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABDE' or orgval == 'abde':
                    p0s4op6 = PhotoImage(file='pics2/p0s4op6.png')
                    change_img(image_label, p0s4op6)
                    change_text(valvesOutput, "5, 6, 9, 12, 14, 17")
                    change_text(serialOutput, "A, B, D, E")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ADEF' or orgval == 'adef':
                    p0s4op7 = PhotoImage(file='pics2/p0s4op7.png')
                    change_img(image_label, p0s4op7)
                    change_text(valvesOutput, "3, 5, 7, 9, 12, 13")
                    change_text(serialOutput, "A, D, E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABCF' or orgval == 'abcf':
                    p0s4op8 = PhotoImage(file='pics2/p0s4op8.png')
                    change_img(image_label, p0s4op8)
                    change_text(valvesOutput, "6, 7, 10, 12, 14, 16")
                    change_text(serialOutput, "A, B, C, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BCEF' or orgval == 'bcef':
                    p0s4op9 = PhotoImage(file='pics2/p0s4op9.png')
                    change_img(image_label, p0s4op9)
                    change_text(valvesOutput, "2, 5, 7, 10, 13, 14")
                    change_text(serialOutput, "B, C, E, F")
                    change_text(paralOutput, "")
                    return

            if serval == '5':
                if orgval == 'BCDEF' or orgval == 'bcdef' or orgval == '':
                    p0s5op1 = PhotoImage(file='pics2/p0s5op1.png')
                    change_img(image_label, p0s5op1)
                    change_text(valvesOutput, "2, 5, 6, 13, 14")
                    change_text(serialOutput, "B, C, D, E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ACDEF' or orgval == 'acdef':
                    p0s5op2 = PhotoImage(file='pics2/p0s5op2.png')
                    change_img(image_label, p0s5op2)
                    change_text(valvesOutput, "3, 6, 7, 12, 13")
                    change_text(serialOutput, "A, C, D, E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABCDE' or orgval == 'abcde':
                    p0s5op3 = PhotoImage(file='pics2/p0s5op3.png')
                    change_img(image_label, p0s5op3)
                    change_text(valvesOutput, "5, 6, 13, 14, 17")
                    change_text(serialOutput, "A, B, C, D, E")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABCDF' or orgval == 'abcdf':
                    p0s5op4 = PhotoImage(file='pics2/p0s5op4.png')
                    change_img(image_label, p0s5op4)
                    change_text(valvesOutput, "6, 7, 12, 13, 16")
                    change_text(serialOutput, "A, B, C, D, F")
                    change_text(paralOutput, "")
                    return

            if serval == '6':
                p0s6 = PhotoImage(file='pics2/p0s6.png')
                change_img(image_label, p0s6)
                change_text(valvesOutput, "5, 6, 13, 14")
                change_text(serialOutput, "A, B, C, D, E, F")
                change_text(paralOutput, "")
                return

        if parval == '2':
            if serval == '0' or serval == '':
                if orgval == 'AC' or orgval == 'ac' or orgval == '':
                    p2s0op1 = PhotoImage(file='pics2/p2s0op1.png')
                    change_img(image_label, p2s0op1)
                    change_text(valvesOutput, "3, 5, 10, 12, 13")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, C")
                    return
                if orgval == 'BD' or orgval == 'bd':
                    p2s0op2 = PhotoImage(file='pics2/p2s0op2.png')
                    change_img(image_label, p2s0op2)
                    change_text(valvesOutput, "2, 7, 9, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, D")
                    return
                if orgval == 'DF' or orgval == 'df':
                    p2s0op3 = PhotoImage(file='pics2/p2s0op3.png')
                    change_img(image_label, p2s0op3)
                    change_text(valvesOutput, "6, 7, 9, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "D, F")
                    return
                if orgval == 'CE' or orgval == 'ce':
                    p2s0op4 = PhotoImage(file='pics2/p2s0op4.png')
                    change_img(image_label, p2s0op4)
                    change_text(valvesOutput, "5, 6, 10, 12, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "C, E")
                    return
                if orgval == 'AB' or orgval == 'ab':
                    p2s0op5 = PhotoImage(file='pics2/p2s0op5.png')
                    change_img(image_label, p2s0op5)
                    change_text(valvesOutput, "5, 6, 7")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B")
                    return
                if orgval == 'EF' or orgval == 'ef':
                    p2s0op6 = PhotoImage(file='pics2/p2s0op6.png')
                    change_img(image_label, p2s0op6)
                    change_text(valvesOutput, "12, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "E, F")
                    return
                if orgval == 'AD' or orgval == 'ad':
                    p2s0op7 = PhotoImage(file='pics2/p2s0op7.png')
                    change_img(image_label, p2s0op7)
                    change_text(valvesOutput, "3, 5, 7, 9, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, D")
                    return
                if orgval == 'AF' or orgval == 'af':
                    p2s0op8 = PhotoImage(file='pics2/p2s0op8.png')
                    change_img(image_label, p2s0op8)
                    change_text(valvesOutput, "3, 5, 9, 10, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, F")
                    return
                if orgval == 'BC' or orgval == 'bc':
                    p2s0op9 = PhotoImage(file='pics2/p2s0op9.png')
                    change_img(image_label, p2s0op9)
                    change_text(valvesOutput, "2, 5, 7, 10, 12, 13")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, C")
                    return
                if orgval == 'CF' or orgval == 'cf':
                    p2s0op10 = PhotoImage(file='pics2/p2s0op10.png')
                    change_img(image_label, p2s0op10)
                    change_text(valvesOutput, "5, 6, 10, 12 ,14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "C, F")
                    return
                if orgval == 'DE' or orgval == 'de':
                    p2s0op11 = PhotoImage(file='pics2/p2s0op11.png')
                    change_img(image_label, p2s0op11)
                    change_text(valvesOutput, "6, 7, 9, 12, 14, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "D, E")
                    return
                if orgval == 'BE' or orgval == 'be':
                    p2s0op12 = PhotoImage(file='pics2/p2s0op12.png')
                    change_img(image_label, p2s0op12)
                    change_text(valvesOutput, "2, 7, 9, 10, 12, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, E")
                    return

            if serval == '1':
                if orgval == 'ABD' or orgval == 'abd' or orgval == '':
                    p2s1op1 = PhotoImage(file='pics2/p2s1op1.png')
                    change_img(image_label, p2s1op1)
                    change_text(valvesOutput, "5, 9, 13, 14")
                    change_text(serialOutput, "A")
                    change_text(paralOutput, "B, D")
                    return
                if orgval == 'DEF' or orgval == 'def':
                    p2s1op2 = PhotoImage(file='pics2/p2s1op2.png')
                    change_img(image_label, p2s1op2)
                    change_text(valvesOutput, "6, 7, 9, 12, 14")
                    change_text(serialOutput, "E")
                    change_text(paralOutput, "D, F")
                    return
                if orgval == 'ABC' or orgval == 'abc':
                    p2s1op3 = PhotoImage(file='pics2/p2s1op3.png')
                    change_img(image_label, p2s1op3)
                    change_text(valvesOutput, "5, 7, 10, 12, 13")
                    change_text(serialOutput, "B")
                    change_text(paralOutput, "A, C")
                    return
                if orgval == 'CEF' or orgval == 'cef':
                    p2s1op4 = PhotoImage(file='pics2/p2s1op4.png')
                    change_img(image_label, p2s1op4)
                    change_text(valvesOutput, "5, 6, 10, 12, 14")
                    change_text(serialOutput, "F")
                    change_text(paralOutput, "C, E")
                    return
                if orgval == 'ABF' or orgval == 'abf':
                    p2s1op5 = PhotoImage(file='pics2/p2s1op5.png')
                    change_img(image_label, p2s1op5)
                    change_text(valvesOutput, "5, 7, 9, 10, 14, 16")
                    change_text(serialOutput, "A")
                    change_text(paralOutput, "B, F")
                    return
                if orgval == 'BEF' or orgval == 'bef':
                    p2s1op6 = PhotoImage(file='pics2/p2s1op6.png')
                    change_img(image_label, p2s1op6)
                    change_text(valvesOutput, "2, 7, 9, 10, 12, 14")
                    change_text(serialOutput, "E")
                    change_text(paralOutput, "B, F")
                    return
                if orgval == 'ABE' or orgval == 'abe':
                    p2s1op7 = PhotoImage(file='pics2/p2s1op7.png')
                    change_img(image_label, p2s1op7)
                    change_text(valvesOutput, "5, 7, 9, 10, 12, 17")
                    change_text(serialOutput, "B")
                    change_text(paralOutput, "A, E")
                    return
                if orgval == 'AEF' or orgval == 'aef':
                    p2s1op8 = PhotoImage(file='pics2/p2s1op8.png')
                    change_img(image_label, p2s1op8)
                    change_text(valvesOutput, "3, 5, 9, 10, 12, 14")
                    change_text(serialOutput, "F")
                    change_text(paralOutput, "A, E")
                    return
                if orgval == 'BCD' or orgval == 'bcd':
                    p2s1op9 = PhotoImage(file='pics2/p2s1op9.png')
                    change_img(image_label, p2s1op9)
                    change_text(valvesOutput, "2, 5, 7, 12, 13, 14")
                    change_text(serialOutput, "C")
                    change_text(paralOutput, "B, D")
                    return
                if orgval == 'CDF' or orgval == 'cdf':
                    p2s1op10 = PhotoImage(file='pics2/p2s1op10.png')
                    change_img(image_label, p2s1op10)
                    change_text(valvesOutput, "5, 6, 7, 12, 14, 16")
                    change_text(serialOutput, "C")
                    change_text(paralOutput, "D, F")
                    return
                if orgval == 'ACD' or orgval == 'acd':
                    p2s1op11 = PhotoImage(file='pics2/p2s1op11.png')
                    change_img(image_label, p2s1op11)
                    change_text(valvesOutput, "3, 5, 7, 12, 13, 14")
                    change_text(serialOutput, "D")
                    change_text(paralOutput, "A, C")
                    return
                if orgval == 'CDE' or orgval == 'cde':
                    p2s1op12 = PhotoImage(file='pics2/p2s1op12.png')
                    change_img(image_label, p2s1op12)
                    change_text(valvesOutput, "5, 6, 7, 12, 14, 17")
                    change_text(serialOutput, "D")
                    change_text(paralOutput, "C, E")
                    return
                if orgval == 'ADE' or orgval == 'ade':
                    p2s1op13 = PhotoImage(file='pics2/p2s1op13.png')
                    change_img(image_label, p2s1op13)
                    change_text(valvesOutput, "3, 5, 7, 9, 12, 14, 17")
                    change_text(serialOutput, "D")
                    change_text(paralOutput, "A, E")
                    return
                if orgval == 'BCF' or orgval == 'bcf':
                    p2s1op14 = PhotoImage(file='pics2/p2s1op14.png')
                    change_img(image_label, p2s1op14)
                    change_text(valvesOutput, "2, 5, 7, 10, 12, 14, 16")
                    change_text(serialOutput, "C")
                    change_text(paralOutput, "B, F")
                    return

            if serval == '2':
                if orgval == 'ABDF' or orgval == 'abdf' or orgval == '':
                    p2s2op1 = PhotoImage(file='pics2/p2s2op1.png')
                    change_img(image_label, p2s2op1)
                    change_text(valvesOutput, "5, 6, 9, 16")
                    change_text(serialOutput, "A, B")
                    change_text(paralOutput, "D, F")
                    return
                if orgval == 'BDEF' or orgval == 'bdef':
                    p2s2op2 = PhotoImage(file='pics2/p2s2op2.png')
                    change_img(image_label, p2s2op2)
                    change_text(valvesOutput, "2, 9, 12, 13")
                    change_text(serialOutput, "E, F")
                    change_text(paralOutput, "B, D")
                    return
                if orgval == 'ABCE' or orgval == 'abce':
                    p2s2op3 = PhotoImage(file='pics2/p2s2op3.png')
                    change_img(image_label, p2s2op3)
                    change_text(valvesOutput, "6, 7, 10, 17")
                    change_text(serialOutput, "A, B")
                    change_text(paralOutput, "C, E")
                    return
                if orgval == 'ACEF' or orgval == 'acef':
                    p2s2op4 = PhotoImage(file='pics2/p2s2op4.png')
                    change_img(image_label, p2s2op4)
                    change_text(valvesOutput, "3, 10, 13, 14")
                    change_text(serialOutput, "E, F")
                    change_text(paralOutput, "A, C")
                    return

            if serval == '3':
                if orgval == 'ABCDE' or orgval == 'abcde' or orgval == '':
                    p2s3op1 = PhotoImage(file='pics2/p2s3op1.png')
                    change_img(image_label, p2s3op1)
                    change_text(valvesOutput, "5, 6, 12, 14, 17")
                    change_text(serialOutput, "A, B, D")
                    change_text(paralOutput, "C, E")
                    return
                if orgval == 'ACDEF' or orgval == 'acdef':
                    p2s3op2 = PhotoImage(file='pics2/p2s3op2.png')
                    change_img(image_label, p2s3op2)
                    change_text(valvesOutput, "3, 5, 7, 12, 13")
                    change_text(serialOutput, "D, E, F")
                    change_text(paralOutput, "A, C")
                    return
                if orgval == 'ABCDF' or orgval == 'abcdf':
                    p2s3op3 = PhotoImage(file='pics2/p2s3op3.png')
                    change_img(image_label, p2s3op3)
                    change_text(valvesOutput, "6, 7, 12, 14, 16")
                    change_text(serialOutput, "A, B, C")
                    change_text(paralOutput, "D, F")
                    return
                if orgval == 'BCDEF' or orgval == 'bcdef':
                    p2s3op4 = PhotoImage(file='pics2/p2s3op4.png')
                    change_img(image_label, p2s3op4)
                    change_text(valvesOutput, "3, 5, 7, 12, 13")
                    change_text(serialOutput, "C, E, F")
                    change_text(paralOutput, "B, D")
                    return
                if orgval == 'ABCEF' or orgval == 'abcef':
                    p2s3op5 = PhotoImage(file='pics2/p2s3op5.png')
                    change_img(image_label, p2s3op5)
                    change_text(valvesOutput, "5, 10, 11, 12, 13")
                    change_text(serialOutput, "B, E, F")
                    change_text(paralOutput, "A, C")
                    return
                if orgval == 'ABDEF' or orgval == 'abdef':
                    p2s3op6 = PhotoImage(file='pics2/p2s3op6.png')
                    change_img(image_label, p2s3op6)
                    change_text(valvesOutput, "7, 8, 9, 13, 14")
                    change_text(serialOutput, "A, E, F")
                    change_text(paralOutput, "B, D")
                    return

        if parval == '3':
            if serval == '0' or serval == '':
                if orgval == 'ACE' or orgval == 'ace' or orgval == '':
                    p3s0op1 = PhotoImage(file='pics2/p3s0op1.png')
                    change_img(image_label, p3s0op1)
                    change_text(valvesOutput, "3, 10, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, C, E")
                    return
                if orgval == 'BDF' or orgval == 'bdf':
                    p3s0op2 = PhotoImage(file='pics2/p3s0op2.png')
                    change_img(image_label, p3s0op2)
                    change_text(valvesOutput, "2, 9, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, D, F")
                    return
                if orgval == 'ABC' or orgval == 'abc':
                    p3s0op3 = PhotoImage(file='pics2/p3s0op3.png')
                    change_img(image_label, p3s0op3)
                    change_text(valvesOutput, "5, 7, 10, 12, 13")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, C")
                    return
                if orgval == 'ABD' or orgval == 'abd':
                    p3s0op4 = PhotoImage(file='pics2/p3s0op4.png')
                    change_img(image_label, p3s0op4)
                    change_text(valvesOutput, "5, 7, 9, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, D")
                    return
                if orgval == 'CEF' or orgval == 'cef':
                    p3s0op5 = PhotoImage(file='pics2/p3s0op5.png')
                    change_img(image_label, p3s0op5)
                    change_text(valvesOutput, "5, 6, 10, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "C, E, F")
                    return
                if orgval == 'DEF' or orgval == 'def':
                    p3s0op6 = PhotoImage(file='pics2/p3s0op6.png')
                    change_img(image_label, p3s0op6)
                    change_text(valvesOutput, "6, 7, 9, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "D, E, F")
                    return
                if orgval == 'ABF' or orgval == 'abf':
                    p3s0op7 = PhotoImage(file='pics2/p3s0op7.png')
                    change_img(image_label, p3s0op7)
                    change_text(valvesOutput, "5, 7, 9, 10, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, F")
                    return
                if orgval == 'BEF' or orgval == 'bef':
                    p3s0op8 = PhotoImage(file='pics2/p3s0op8.png')
                    change_img(image_label, p3s0op8)
                    change_text(valvesOutput, "2, 7, 9, 10, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, E, F")
                    return
                if orgval == 'ABE' or orgval == 'abe':
                    p3s0op9 = PhotoImage(file='pics2/p3s0op9.png')
                    change_img(image_label, p3s0op9)
                    change_text(valvesOutput, "5, 7, 9, 10, 12, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, E")
                    return
                if orgval == 'AEF' or orgval == 'aef':
                    p3s0op10 = PhotoImage(file='pics2/p3s0op10.png')
                    change_img(image_label, p3s0op10)
                    change_text(valvesOutput, "3, 5, 9, 10, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, E, F")
                    return
                if orgval == 'BCD' or orgval == 'bcd':
                    p3s0op11 = PhotoImage(file='pics2/p3s0op11.png')
                    change_img(image_label, p3s0op11)
                    change_text(valvesOutput, "2, 5, 7, 12, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, C, D")
                    return
                if orgval == 'CDF' or orgval == 'cdf':
                    p3s0op12 = PhotoImage(file='pics2/p3s0op12.png')
                    change_img(image_label, p3s0op12)
                    change_text(valvesOutput, "5, 6, 7, 12, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "C, D, F")
                    return
                if orgval == 'ACD' or orgval == 'acd':
                    p3s0op13 = PhotoImage(file='pics2/p3s0op13.png')
                    change_img(image_label, p3s0op13)
                    change_text(valvesOutput, "3, 5, 7, 12, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, C, D")
                    return
                if orgval == 'CDE' or orgval == 'cde':
                    p3s0op14 = PhotoImage(file='pics2/p3s0op14.png')
                    change_img(image_label, p3s0op14)
                    change_text(valvesOutput, "5, 6, 7, 12, 14, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "C, D, E")
                    return
                if orgval == 'ADE' or orgval == 'ade':
                    p3s0op15 = PhotoImage(file='pics2/p3s0op15.png')
                    change_img(image_label, p3s0op15)
                    change_text(valvesOutput, "3, 5, 7, 9, 12, 14, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, D, E")
                    return
                if orgval == 'BCF' or orgval == 'bcf':
                    p3s0op16 = PhotoImage(file='pics2/p3s0op16.png')
                    change_img(image_label, p3s0op16)
                    change_text(valvesOutput, "2, 5, 7, 10, 12, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, C, F")
                    return
                if orgval == 'ADF' or orgval == 'adf':
                    p3s0op17 = PhotoImage(file='pics2/p3s0op17.png')
                    change_img(image_label, p3s0op17)
                    change_text(valvesOutput, "3, 5, 7, 9, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, D, F")
                    return
                if orgval == 'BCE' or orgval == 'bce':
                    p3s0op18 = PhotoImage(file='pics2/p3s0op18.png')
                    change_img(image_label, p3s0op18)
                    change_text(valvesOutput, "2, 5, 7, 10, 12, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, C, E")
                    return
                if orgval == 'ACF' or orgval == 'acf':
                    p3s0op19 = PhotoImage(file='pics2/p3s0op19.png')
                    change_img(image_label, p3s0op19)
                    change_text(valvesOutput, "3, 5, 10, 12, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, C, F")
                    return
                if orgval == 'BDE' or orgval == 'bde':
                    p3s0op20 = PhotoImage(file='pics2/p3s0op20.png')
                    change_img(image_label, p3s0op20)
                    change_text(valvesOutput, "2, 7, 9, 12, 14, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, D, E")
                    return

            if serval == '1':
                if orgval == 'ACEF' or orgval == 'acef' or orgval == '':
                    p3s1op1 = PhotoImage(file='pics2/p3s1op1.png')
                    change_img(image_label, p3s1op1)
                    change_text(valvesOutput, "3, 10, 14")
                    change_text(serialOutput, "F")
                    change_text(paralOutput, "A, C, E")
                    return
                if orgval == 'ACDE' or orgval == 'acde':
                    p3s1op2 = PhotoImage(file='pics2/p3s1op2.png')
                    change_img(image_label, p3s1op2)
                    change_text(valvesOutput, "3, 7, 14, 17")
                    change_text(serialOutput, "D")
                    change_text(paralOutput, "A, C, E")
                    return
                if orgval == 'ABCE' or orgval == 'abce':
                    p3s1op3 = PhotoImage(file='pics2/p3s1op3.png')
                    change_img(image_label, p3s1op3)
                    change_text(valvesOutput, "7, 10, 17")
                    change_text(serialOutput, "B")
                    change_text(paralOutput, "A, C, E")
                    return
                if orgval == 'BDEF' or orgval == 'bdef':
                    p3s1op4 = PhotoImage(file='pics2/p3s1op4.png')
                    change_img(image_label, p3s1op4)
                    change_text(valvesOutput, "2, 9, 12")
                    change_text(serialOutput, "E")
                    change_text(paralOutput, "B, D, F")
                    return
                if orgval == 'BCDF' or orgval == 'bcdf':
                    p3s1op5 = PhotoImage(file='pics2/p3s1op5.png')
                    change_img(image_label, p3s1op5)
                    change_text(valvesOutput, "2, 5, 12, 16")
                    change_text(serialOutput, "C")
                    change_text(paralOutput, "B, D, F")
                    return
                if orgval == 'ABDF' or orgval == 'abdf':
                    p3s1op6 = PhotoImage(file='pics2/p3s1op6.png')
                    change_img(image_label, p3s1op6)
                    change_text(valvesOutput, "5,  9, 16")
                    change_text(serialOutput, "A")
                    change_text(paralOutput, "B, D, F")
                    return

            if serval == '2':
                if orgval == 'ABCDF' or orgval == 'abcdf' or orgval == '':
                    p3s2op1 = PhotoImage(file='pics2/p3s2op1.png')
                    change_img(image_label, p3s2op1)
                    change_text(valvesOutput, "5, 12, 16")
                    change_text(serialOutput, "A, C")
                    change_text(paralOutput, "B, D, F")
                    return
                if orgval == 'ABDEF' or orgval == 'abdef':
                    p3s2op2 = PhotoImage(file='pics2/p3s2op2.png')
                    change_img(image_label, p3s2op2)
                    change_text(valvesOutput, "5, 9, 12")
                    change_text(serialOutput, "A, E")
                    change_text(paralOutput, "B, D, F")
                    return
                if orgval == 'BCDEF' or orgval == 'bcdef':
                    p3s2op3 = PhotoImage(file='pics2/p3s2op3.png')
                    change_img(image_label, p3s2op3)
                    change_text(valvesOutput, "2, 5, 12")
                    change_text(serialOutput, "C, E")
                    change_text(paralOutput, "B, D, F")
                    return
                if orgval == 'ACDEF' or orgval == 'acdef':
                    p3s2op4 = PhotoImage(file='pics2/p3s2op4.png')
                    change_img(image_label, p3s2op4)
                    change_text(valvesOutput, "3, 7, 14")
                    change_text(serialOutput, "D, F")
                    change_text(paralOutput, "A, C, E")
                    return
                if orgval == 'ABCDE' or orgval == 'abcde':
                    p3s2op5 = PhotoImage(file='pics2/p3s2op5.png')
                    change_img(image_label, p3s2op5)
                    change_text(valvesOutput, "7, 14, 17")
                    change_text(serialOutput, "B, D")
                    change_text(paralOutput, "A, C, E")
                    return
                if orgval == 'ABCEF' or orgval == 'abcef':
                    p3s2op6 = PhotoImage(file='pics2/p3s2op6.png')
                    change_img(image_label, p3s2op6)
                    change_text(valvesOutput, "7, 10, 14")
                    change_text(serialOutput, "B, F")
                    change_text(paralOutput, "A, C, E")
                    return
        if parval == '4':
            if serval == '0' or serval == '':
                if orgval == 'ABCD' or orgval == 'abcd' or orgval == '':
                    p4s0op1 = PhotoImage(file='pics2/p4s0op1.png')
                    change_img(image_label, p4s0op1)
                    change_text(valvesOutput, "5, 7, 12, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, C, D")
                    return
                if orgval == 'ABEF' or orgval == 'abef':
                    p4s0op2 = PhotoImage(file='pics2/p4s0op2.png')
                    change_img(image_label, p4s0op2)
                    change_text(valvesOutput, "5, 7, 9, 10, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, E, F")
                    return
                if orgval == 'CDEF' or orgval == 'cdef':
                    p4s0op3 = PhotoImage(file='pics2/p4s0op3.png')
                    change_img(image_label, p4s0op3)
                    change_text(valvesOutput, "5, 6, 7, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "C, D, E, F")
                    return
                if orgval == 'ABDF' or orgval == 'abdf':
                    p4s0op4 = PhotoImage(file='pics2/p4s0op4.png')
                    change_img(image_label, p4s0op4)
                    change_text(valvesOutput, "5, 7, 9, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, D, F")
                    return
                if orgval == 'BCDF' or orgval == 'bcdf':
                    p4s0op5 = PhotoImage(file='pics2/p4s0op5.png')
                    change_img(image_label, p4s0op5)
                    change_text(valvesOutput, "2, 5, 7, 12, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, C, D, F")
                    return
                if orgval == 'BDEF' or orgval == 'bdef':
                    p4s0op6 = PhotoImage(file='pics2/p4s0op6.png')
                    change_img(image_label, p4s0op6)
                    change_text(valvesOutput, "2, 7, 9, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, D, E, F")
                    return
                if orgval == 'ABCE' or orgval == 'abce':
                    p4s0op7 = PhotoImage(file='pics2/p4s0op7.png')
                    change_img(image_label, p4s0op7)
                    change_text(valvesOutput, "5, 7, 10, 12, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, C, E")
                    return
                if orgval == 'ACDE' or orgval == 'acde':
                    p4s0op8 = PhotoImage(file='pics2/p4s0op8.png')
                    change_img(image_label, p4s0op8)
                    change_text(valvesOutput, "3, 5, 7, 12, 14, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, C, D, E")
                    return
                if orgval == 'ACEF' or orgval == 'acef':
                    p4s0op9 = PhotoImage(file='pics2/p4s0op9.png')
                    change_img(image_label, p4s0op9)
                    change_text(valvesOutput, "3, 5, 10, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, C, E, F")
                    return
                if orgval == 'ABDE' or orgval == 'abde':
                    p4s0op10 = PhotoImage(file='pics2/p4s0op10.png')
                    change_img(image_label, p4s0op10)
                    change_text(valvesOutput, "5, 7, 9, 12, 14, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, D, E")
                    return
                if orgval == 'ADEF' or orgval == 'adef':
                    p4s0op11 = PhotoImage(file='pics2/p4s0op11.png')
                    change_img(image_label, p4s0op11)
                    change_text(valvesOutput, "3, 5, 7, 9, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, D, E, F")
                    return
                if orgval == 'ABCF' or orgval == 'abcf':
                    p4s0op12 = PhotoImage(file='pics2/p4s0op12.png')
                    change_img(image_label, p4s0op12)
                    change_text(valvesOutput, "5, 7, 10, 12, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, C, F")
                    return
                if orgval == 'BCEF' or orgval == 'bcef':
                    p4s0op13 = PhotoImage(file='pics2/p4s0op13.png')
                    change_img(image_label, p4s0op13)
                    change_text(valvesOutput, "2, 5, 7, 10, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, C, E, F")
                    return
                if orgval == 'ACDF' or orgval == 'acdf':
                    p4s0op14 = PhotoImage(file='pics2/p4s0op14.png')
                    change_img(image_label, p4s0op14)
                    change_text(valvesOutput, "3, 5, 7, 12, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, C, D, F")
                    return
                if orgval == 'BCDE' or orgval == 'bcde':
                    p4s0op15 = PhotoImage(file='pics2/p4s0op15.png')
                    change_img(image_label, p4s0op15)
                    change_text(valvesOutput, "2, 5, 7, 12, 14, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, C, D, E")
                    return

            if serval == '1':
                if orgval == 'ACDEF' or orgval == 'acdef' or orgval == '':
                    p4s1op1 = PhotoImage(file='pics2/p4s1op1.png')
                    change_img(image_label, p4s1op1)
                    change_text(valvesOutput, "3, 5, 7, 12, 14")
                    change_text(serialOutput, "A")
                    change_text(paralOutput, "C, D, E, F")
                    return
                if orgval == 'BCDEF' or orgval == 'bcdef':
                    p4s1op2 = PhotoImage(file='pics2/p4s1op2.png')
                    change_img(image_label, p4s1op2)
                    change_text(valvesOutput, "2, 5, 7, 12, 14")
                    change_text(serialOutput, "B")
                    change_text(paralOutput, "C, D, E, F")
                    return
                if orgval == 'ABCDF' or orgval == 'abcdf':
                    p4s1op3 = PhotoImage(file='pics2/p4s1op3.png')
                    change_img(image_label, p4s1op3)
                    change_text(valvesOutput, "5, 7, 12, 14, 16")
                    change_text(serialOutput, "F")
                    change_text(paralOutput, "A, B, C, D")
                    return
                if orgval == 'ABCDE' or orgval == 'abcde':
                    p4s1op1 = PhotoImage(file='pics2/p4s1op1.png')
                    change_img(image_label, p4s1op1)
                    change_text(valvesOutput, "5, 7, 12, 14, 17")
                    change_text(serialOutput, "E")
                    change_text(paralOutput, "A, B, C, D")
                    return
                if orgval == 'ABDEF' or orgval == 'abdef':
                    p4s1op5 = PhotoImage(file='pics2/p4s1op5.png')
                    change_img(image_label, p4s1op5)
                    change_text(valvesOutput, "5, 7, 9, 12, 14")
                    change_text(serialOutput, "A")
                    change_text(paralOutput, "B, D, E, F")
                    return
                if orgval == 'ABCEF' or orgval == 'abcef':
                    p4s1op6 = PhotoImage(file='pics2/p4s1op6.png')
                    change_img(image_label, p4s1op6)
                    change_text(valvesOutput, "5, 7, 10, 12, 14")
                    change_text(serialOutput, "B")
                    change_text(paralOutput, "A, C, E, F")
                    return

        if parval == '5':
            if serval == '0' or serval == '':
                if orgval == 'ACDEF' or orgval == 'acdef' or orgval == '':
                    p5s0op1 = PhotoImage(file='pics2/p5s0op1.png')
                    change_img(image_label, p5s0op1)
                    change_text(valvesOutput, "3, 5, 7, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, C, D, E, F")
                    return
                if orgval == 'BCDEF' or orgval == 'bcdef':
                    p5s0op2 = PhotoImage(file='pics2/p5s0op2.png')
                    change_img(image_label, p5s0op2)
                    change_text(valvesOutput, "2, 5, 7, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "B, C, D, E, F")
                    return
                if orgval == 'ABDEF' or orgval == 'abdef':
                    p5s0op3 = PhotoImage(file='pics2/p5s0op3.png')
                    change_img(image_label, p5s0op3)
                    change_text(valvesOutput, "5, 7, 9, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, D, E, F")
                    return
                if orgval == 'ABCEF' or orgval == 'abcef':
                    p5s0op4 = PhotoImage(file='pics2/p5s0op4.png')
                    change_img(image_label, p5s0op4)
                    change_text(valvesOutput, "5, 7, 10, 12, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, C, E, F")
                    return
                if orgval == 'ABCDF' or orgval == 'abcdf':
                    p5s0op5 = PhotoImage(file='pics2/p5s0op5.png')
                    change_img(image_label, p5s0op5)
                    change_text(valvesOutput, "5, 7, 12, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, C, D, F")
                    return
                if orgval == 'ABCDE' or orgval == 'abcde':
                    p5s0op6 = PhotoImage(file='pics2/p5s0op6.png')
                    change_img(image_label, p5s0op6)
                    change_text(valvesOutput, "5, 7, 12, 14, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "A, B, C, D, E")
                    return

        if parval == '6':
            if serval == '0' or serval == '':
                p6s0 = PhotoImage(file='pics2/p6s0.png')
                change_img(image_label, p6s0)
                change_text(valvesOutput, "5, 7, 12, 14")
                change_text(serialOutput, "")
                change_text(paralOutput, "A, B, C, D, E, F")
                return

    if setval == '2':
        if parval == '0' or parval == '':
            if serval == '2':
                if orgval == 'ABEF' or orgval == 'abef' or orgval == '':
                    p0s2set2op1 = PhotoImage(file='pics2/p0s2set2op1.png')
                    change_img(image_label, p0s2set2op1)
                    change_text(valvesOutput, "5, 6, 7, 12, 13, 14")
                    change_text(serialOutput, "set 1: A, B  set2: E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'CDEF' or orgval == 'cdef':
                    p0s2set2op2 = PhotoImage(file='pics2/p0s2set2op2.png')
                    change_img(image_label, p0s2set2op2)
                    change_text(valvesOutput, "5, 6, 7, 12, 13, 14")
                    change_text(serialOutput, "set 1: C, D  set2: E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABCD' or orgval == 'abcd':
                    p0s2set2op3 = PhotoImage(file='pics2/p0s2set2op3.png')
                    change_img(image_label, p0s2set2op3)
                    change_text(valvesOutput, "5, 6, 7, 12, 13, 14")
                    change_text(serialOutput, "set 1: A, B  set2: C, D")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ACDF' or orgval == 'acdf':
                    p0s2set2op4 = PhotoImage(file='pics2/p0s2set2op4.png')
                    change_img(image_label, p0s2set2op4)
                    change_text(valvesOutput, "3, 5,7, 12, 14, 16")
                    change_text(serialOutput, "set 1: A, C  set2: D, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BCDE' or orgval == 'bcde':
                    p0s2set2op5 = PhotoImage(file='pics2/p0s2set2op5.png')
                    change_img(image_label, p0s2set2op5)
                    change_text(valvesOutput, "2, 5, 7, 12, 14, 17")
                    change_text(serialOutput, "set 1: B, D  set2: C, E")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ACEF' or orgval == 'acef':
                    p0s2set2op6 = PhotoImage(file='pics2/p0s2set2op6.png')
                    change_img(image_label, p0s2set2op6)
                    change_text(valvesOutput, "3, 5, 10, 12, 13, 14")
                    change_text(serialOutput, "set 1: A, C  set2: E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BDEF' or orgval == 'bdef':
                    p0s2set2op7 = PhotoImage(file='pics2/p0s2set2op7.png')
                    change_img(image_label, p0s2set2op7)
                    change_text(valvesOutput, "2, 7, 9, 12, 13, 14")
                    change_text(serialOutput, "set 1: B, D  set2: E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABCE' or orgval == 'abce':
                    p0s2set2op8 = PhotoImage(file='pics2/p0s2set2op8.png')
                    change_img(image_label, p0s2set2op8)
                    change_text(valvesOutput, "5, 6, 7, 10, 12, 17")
                    change_text(serialOutput, "set 1: A, B  set2: C, E")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABDF' or orgval == 'abdf':
                    p0s2set2op9 = PhotoImage(file='pics2/p0s2set2op9.png')
                    change_img(image_label, p0s2set2op9)
                    change_text(valvesOutput, "5, 6, 7, 9, 14, 16")
                    change_text(serialOutput, "set 1: A, B  set2: D, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABCF' or orgval == 'abcf':
                    p0s2set2op10 = PhotoImage(file='pics2/p0s2set2op10.png')
                    change_img(image_label, p0s2set2op10)
                    change_text(valvesOutput, "5, 6, 7, 10, 12, 14, 16")
                    change_text(serialOutput, "set 1: A, B  set2: C, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ABDE' or orgval == 'abde':
                    p0s2set2op11 = PhotoImage(file='pics2/p0s2set2op11.png')
                    change_img(image_label, p0s2set2op11)
                    change_text(valvesOutput, "5, 6, 7, 9, 12, 14, 17")
                    change_text(serialOutput, "set 1: A, B  set2: D, E")
                    change_text(paralOutput, "")
                    return
                if orgval == 'BCEF' or orgval == 'bcef':
                    p0s2set2op12 = PhotoImage(file='pics2/p0s2set2op12.png')
                    change_img(image_label, p0s2set2op12)
                    change_text(valvesOutput, "2, 5, 7, 10, 12, 13, 14")
                    change_text(serialOutput, "set 1: B, C  set2: E, F")
                    change_text(paralOutput, "")
                    return
                if orgval == 'ADEF' or orgval == 'adef':
                    p0s2set2op13 = PhotoImage(file='pics2/p0s2set2op13.png')
                    change_img(image_label, p0s2set2op13)
                    change_text(valvesOutput, "3, 5, 7, 9, 12, 13, 14")
                    change_text(serialOutput, "set 1: A, D  set2: E, F")
                    change_text(paralOutput, "")
                    return

        if parval == '2':
            if serval == '0' or serval == '':
                if orgval == 'ABEF' or orgval == 'abef' or orgval == '':
                    p2s0set2op1 = PhotoImage(file='pics2/p2s0set2op1.png')
                    change_img(image_label, p2s0set2op1)
                    change_text(valvesOutput, "5, 6, 7, 12, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: A, B  set2: E, F")
                    return
                if orgval == 'CDEF' or orgval == 'cdef':
                    p2s0set2op2 = PhotoImage(file='pics2/p2s0set2op2.png')
                    change_img(image_label, p2s0set2op2)
                    change_text(valvesOutput, "5, 6, 7, 12, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: C, D  set2: E, F")
                    return
                if orgval == 'ABCD' or orgval == 'abcd':
                    p2s0set2op3 = PhotoImage(file='pics2/p2s0set2op3.png')
                    change_img(image_label, p2s0set2op3)
                    change_text(valvesOutput, "5, 6, 7, 12, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: A, B  set2: C, D")
                    return
                if orgval == 'ACDF' or orgval == 'acdf':
                    p2s0set2op4 = PhotoImage(file='pics2/p2s0set2op4.png')
                    change_img(image_label, p2s0set2op4)
                    change_text(valvesOutput, "3, 5,7, 12, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: A, C  set2: D, F")
                    return
                if orgval == 'BCDE' or orgval == 'bcde':
                    p2s0set2op5 = PhotoImage(file='pics2/p2s0set2op5.png')
                    change_img(image_label, p2s0set2op5)
                    change_text(valvesOutput, "2, 5, 7, 12, 14, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: B, D  set2: C, E")
                    return
                if orgval == 'ACEF' or orgval == 'acef':
                    p2s0set2op6 = PhotoImage(file='pics2/p2s0set2op6.png')
                    change_img(image_label, p2s0set2op6)
                    change_text(valvesOutput, "3, 5, 10, 12, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: A, C  set2: E, F")
                    return
                if orgval == 'BDEF' or orgval == 'bdef':
                    p2s0set2op7 = PhotoImage(file='pics2/p2s0set2op7.png')
                    change_img(image_label, p2s0set2op7)
                    change_text(valvesOutput, "2, 7, 9, 12, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: B, D  set2: E, F")
                    return
                if orgval == 'ABCE' or orgval == 'abce':
                    p2s0set2op8 = PhotoImage(file='pics2/p2s0set2op8.png')
                    change_img(image_label, p2s0set2op8)
                    change_text(valvesOutput, "5, 6, 7, 10, 12, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: A, B  set2: C, E")
                    return
                if orgval == 'ABDF' or orgval == 'abdf':
                    p2s0set2op9 = PhotoImage(file='pics2/p2s0set2op9.png')
                    change_img(image_label, p2s0set2op9)
                    change_text(valvesOutput, "5, 6, 7, 9, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: A, B  set2: D, F")
                    return
                if orgval == 'ABCF' or orgval == 'abcf':
                    p2s0set2op10 = PhotoImage(file='pics2/p2s0set2op10.png')
                    change_img(image_label, p2s0set2op10)
                    change_text(valvesOutput, "5, 6, 7, 10, 12, 14, 16")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: A, B  set2: C, F")
                    return
                if orgval == 'ABDE' or orgval == 'abde':
                    p2s0set2op11 = PhotoImage(file='pics2/p2s0set2op11.png')
                    change_img(image_label, p2s0set2op11)
                    change_text(valvesOutput, "5, 6, 7, 9, 12, 14, 17")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: A, B  set2: D, E")
                    return
                if orgval == 'BCEF' or orgval == 'bcef':
                    p2s0set2op12 = PhotoImage(file='pics2/p2s0set2op12.png')
                    change_img(image_label, p2s0set2op12)
                    change_text(valvesOutput, "2, 5, 7, 10, 12, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: B, C  set2: E, F")
                    return
                if orgval == 'ADEF' or orgval == 'adef':
                    p2s0set2op13 = PhotoImage(file='pics2/p2s0set2op13.png')
                    change_img(image_label, p2s0set2op13)
                    change_text(valvesOutput, "3, 5, 7, 9, 12, 13, 14")
                    change_text(serialOutput, "")
                    change_text(paralOutput, "set 1: A, D  set2: E, F")
                    return
            if serval == '1':
                p2s1set2 = PhotoImage(file='pics2/p2s1set2.png')
                change_img(image_label, p2s1set2)
                change_text(valvesOutput, "5, 7, 12, 14")
                change_text(serialOutput, "set 1: B  set 2: E")
                change_text(paralOutput, "set 1: A, C  set 2: D, F")
                return

        if parval == '3':
            p3s0set2 = PhotoImage(file='pics2/p3s0set2.png')
            change_img(image_label, p3s0set2)
            change_text(valvesOutput, "5, 7, 12, 14")
            change_text(serialOutput, "")
            change_text(paralOutput, "set 1: A, B, C  set 2: D, E, F")
            return

    if setval == '3':
        if parval == '0' or parval == '':
            if serval == '2':
                p0s2set3 = PhotoImage(file='pics2/p0s2set3.png')
                change_img(image_label, p0s2set3)
                change_text(valvesOutput, "5, 6, 7, 12, 13, 14")
                change_text(serialOutput, "set 1: A, B  set 2: C, D  set 3: E, F")
                change_text(paralOutput, "")
                return

    else:
        change_img(image_label, img)
        change_text(valvesOutput, "error")
        change_text(serialOutput, "error")
        change_text(paralOutput, "error")


# run button command
def click(event=None):
    which_valves(pEntry.get(), sEntry.get(), setEntry.get(), orgEntry.get())


root = customtkinter.CTk()
root.geometry("1200x1200")
root.title("Organizer")
root.bind('<Return>', click)
# canvas = Canvas(root, width=900, height=700)
# canvas.pack()

#                                                              #
################################################################
#                                                              #

# input frame: number of organs entries, number of setups, run button
# bg color: R188 G188 B188
inputFrame = customtkinter.CTkFrame(master=root,)
inputFrame.place(relx=0.1, rely=0.1, relwidth=0.4, relheight=0.4)

# input wrapper
input_wrapper_frame = customtkinter.CTkFrame(master=inputFrame,fg_color= "grey")
input_wrapper_frame.place(relx=0.2, rely=0.25, relwidth=0.7, relheight=0.6)

# parallel
pLabel = customtkinter.CTkLabel(input_wrapper_frame, text="Parallel organs:", font=("Helvetica", 25))
pLabel.grid(row=0, column=0, sticky=W)
pEntry = customtkinter.CTkEntry(input_wrapper_frame)
pEntry.grid(row=0, column=1, pady=10)

# serial
sLabel = customtkinter.CTkLabel(input_wrapper_frame, text="Serial organs:")
sLabel.grid(row=1, column=0, sticky=W)
sEntry = customtkinter.CTkEntry(input_wrapper_frame)
sEntry.grid(row=1, column=1, pady=10)

# setups
setupsLabel = customtkinter.CTkLabel(input_wrapper_frame, text="Setups:")
setupsLabel.grid(row=2, column=0, sticky=W)
setEntry = customtkinter.CTkEntry(input_wrapper_frame)
setEntry.grid(row=2, column=1, pady=10)

# organs
organsLabel = customtkinter.CTkLabel(input_wrapper_frame, text="Organs:")
organsLabel.grid(row=3, column=0, sticky=W)
orgEntry = customtkinter.CTkEntry(input_wrapper_frame)
orgEntry.grid(row=3, column=1, pady=10)

# run button fg=red
runButton = customtkinter.CTkButton(input_wrapper_frame, text="Run", command=click, corner_radius=3)
runButton.grid(row=4, column=1, pady=10)

#                                                              #
################################################################
#                                                              #

#
# output frame: which valves to close, which organs
#
outputFrame = customtkinter.CTkFrame(root)
outputFrame.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.4)

output_wrapper_frame = customtkinter.CTkFrame(master=outputFrame,fg_color= "grey")
output_wrapper_frame.place(relx=0.2, rely=0.1, relwidth=0.7, relheight=0.55)

# which valves
valvLabel = customtkinter.CTkLabel(output_wrapper_frame, text="Close valves:")
valvLabel.grid(row=3, column=0, sticky=W)
valvesOutput = customtkinter.CTkLabel(output_wrapper_frame, padx=5, height=3)
valvesOutput.grid(row=4, column=0, sticky=W)

# which organs
serialOrgansLabel = customtkinter.CTkLabel(output_wrapper_frame, text="Serial organs:")
serialOrgansLabel.grid(row=5, column=0, sticky=W)
serialOutput = customtkinter.CTkLabel(output_wrapper_frame, padx=5, height=3)
serialOutput.grid(row=6, column=0, sticky=W)

paralOrgansLabel = customtkinter.CTkLabel(output_wrapper_frame, text="Parallel organs:")
paralOrgansLabel.grid(row=7, column=0, sticky=W)
paralOutput = customtkinter.CTkLabel(output_wrapper_frame, padx=5, height=3)
paralOutput.grid(row=8, column=0, sticky=W)

# image frame - visual representation
imageFrame = customtkinter.CTkFrame(root)
imageFrame.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.8)

img = ImageTk.PhotoImage(Image.open("pics2/main.png"))
image_label = customtkinter.CTkLabel(imageFrame, image=img)
image_label.place(relx=0.25, rely=0.25)

root.mainloop()
