from tkinter import *
from tkinter import ttk
from turtle import down
from library import download_image_from_url, set_desktop_background_image 
from pokeapi import get_pokemon_list, get_pokemmon_image_url
import os
import sys
import ctypes

def main():

    script_dir = sys.path[0]
    image_dir = os.path.join(script_dir, 'images')
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)
    
    
    root = Tk()
    root.title('pokemon Image Viewer')
    
    myappid = 'pokemon.image.viewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    root.iconbitmap(os.path.join(script_dir, 'pokeballicon.ico'))
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
#configuring the size of the program
    frm = ttk.Frame(root)
    frm.grid(sticky=(N,S,E,W))
    frm.rowconfigure(0, weight=1)
    frm.columnconfigure(0, weight=1)
    root.minsize(500, 600)
#creating desktop image
    img_poke = PhotoImage(file=os.path.join(script_dir, 'pokeball.png'))
    lbl_img = ttk.Label (frm, image=img_poke)
    lbl_img.grid(row=0, column=0, padx=10, pady=10)
#creating select pokemon button
    pokemon_list = get_pokemon_list()
    pokemon_list.sort()
    pokemon_list = [p.capitalize() for p in pokemon_list]
    cbo_pokemon = ttk.Combobox(frm, value=pokemon_list, state='readonly')
    cbo_pokemon.set('Select a pokemon')
    cbo_pokemon.grid(row=1, column=0, padx=10, pady=10)
#getting image of pokemon
    def handle_poke_select(event):
        pokemon_name = cbo_pokemon.get()
        image_url = get_pokemmon_image_url(pokemon_name)
        image_path = os.path.join(image_dir, pokemon_name + '.png')
        download_image_from_url(image_url, image_path)
        img_poke['file'] = image_path
        btn_set_desktop.state(['!disabled'])

    cbo_pokemon.bind('<<ComboboxSelected>>', handle_poke_select)
#creating set image as desktop button
    def handle_button_set_desktop():
        pokemon_name = cbo_pokemon.get()
        image_path = os.path.join(image_dir, pokemon_name + '.png')
        set_desktop_background_image(image_path)

    btn_set_desktop = ttk.Button(frm, text='Set as desktop image', command=handle_button_set_desktop)
    btn_set_desktop.state(['disabled'])
    btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)

    root.mainloop()
main()