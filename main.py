from random import choice
from tkinter import ttk, messagebox
import tkinter as tk
import json

# Try to open movies.json, if it doesn't exist, create it
try:
    movie_data = open('movie.json', 'x')
    movie_data.close()

except:
    with open('movies.json', mode = 'r') as movie_r:
        movie_data = json.load(movie_r)


class App:
    def __init__(self, root):
        self.movies = MovieGenerator(movie_data)

        self.root = root

        # Tells window how to handle being resized
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(3, weight=3)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(8, weight=3)

        # Add and configure combo box to select search method
        self.combo = ttk.Combobox(root, values=['Add movie',
                                                'True random',
                                                'Genre random',
                                                'Platform random',
                                                'Rent random',
                                                'Search title'])
        self.combo.set('Select method')
        self.combo.bind('<<ComboboxSelected>>', self.method_changed)

        # Add button to confirm selection
        self.go_button = tk.Button(root, text='Go', padx=3, command=self.use_go_button)

        # Add entries for add_movie method
        self.entry_title = tk.Entry(root)
        self.entry_genre = tk.Entry(root)
        self.entry_platform = tk.Entry(root)
        self.entry_rent = tk.Entry(root)

        # Add labels for entries ^^^
        self.label_title = tk.Label(root, text='Title:')
        self.label_genre = tk.Label(root, text='Genre:')
        self.label_platform = tk.Label(root, text='Platform:')
        self.label_rent = tk.Label(root, text='Rent:')

        # Add text box for output
        self.text = tk.Text(root, width=30, height=7, padx=5, pady=5)

        # Add remove_movie button
        self.remove_button = tk.Button(root, text='Remove movie', command=self.remove_movie2)

        # Add save_and_exit button
        self.save_exit_button = tk.Button(root, text='Save and exit', command=self.save_and_exit)


        # Place necessary items in window
        self.combo.grid(row=1, column=1)
        self.go_button.grid(row=1, column=2, padx=5)
        

    # Change input options based on method selected
    def method_changed(self, event):
        # Remove add_movie entries
        def remove_add_movie():
            self.label_title.grid_remove()
            self.label_genre.grid_remove()
            self.label_platform.grid_remove()
            self.label_rent.grid_remove()

            self.entry_title.grid_remove()
            self.entry_genre.grid_remove()
            self.entry_platform.grid_remove()
            self.entry_rent.grid_remove()

        curr_method = self.combo.get().lower()

        if curr_method == 'add movie':
            # Remove text box
            self.text.grid_remove()

            # Remove remove button
            self.remove_button.grid_remove()

            # Place labels in window
            self.label_title.grid(row=2, column=1)
            self.label_genre.grid(row=3, column=1)
            self.label_platform.grid(row=4, column=1)
            self.label_rent.grid(row=5, column=1)

            # Place entries in window
            self.entry_title.grid(row=2, column=2)
            self.entry_genre.grid(row=3, column=2)
            self.entry_platform.grid(row=4, column=2)
            self.entry_rent.grid(row=5, column=2)

            # Place save and exit button in window
            self.save_exit_button.grid(row=6, column=2)

        elif curr_method == 'true random':
            remove_add_movie()

            # Place text box in window
            self.text.grid(row=6, column=1, columnspan=2)

            # Place save and exit button in window
            self.save_exit_button.grid(row=7, column=2)

            # Place remove movie button
            self.remove_button.grid(row=7, column=1)
        
        elif curr_method == 'genre random':
            remove_add_movie()

            # Place label and entry in window
            self.label_genre.grid(row=3, column=1)
            self.entry_genre.grid(row=3, column=2)

            # Place text box in window
            self.text.grid(row=6, column=1, columnspan=2)

            # Place save and exit button in window
            self.save_exit_button.grid(row=7, column=2)

            # Place remove movie button
            self.remove_button.grid(row=7, column=1)

        elif curr_method == 'platform random':
            remove_add_movie()

            # Place text label and entry in window
            self.label_platform.grid(row=4, column=1)
            self.entry_platform.grid(row=4, column=2)

            # Place text box in window
            self.text.grid(row=6, column=1, columnspan=2)

            # Place save and exit button in window
            self.save_exit_button.grid(row=7, column=2)

            # Place remove movie button
            self.remove_button.grid(row=7, column=1)

        elif curr_method == 'rent random':
            remove_add_movie()

            # Place label and entry in window
            self.label_rent.grid(row=5, column=1)
            self.entry_rent.grid(row=5, column=2)

            # Place text box in window
            self.text.grid(row=6, column=1, columnspan=2)

            # Place save and exit button in window
            self.save_exit_button.grid(row=7, column=2)

            # Place remove movie button
            self.remove_button.grid(row=7, column=1)

        elif curr_method == 'search title':
            remove_add_movie()

            # Place label and entry in window
            self.label_title.grid(row=2, column=1)
            self.entry_title.grid(row=2, column=2)

            # Place text box in window
            self.text.grid(row=6, column=1, columnspan=2)

            # Place save and exit button in window
            self.save_exit_button.grid(row=7, column=2)

            # Place remove movie button
            self.remove_button.grid(row=7, column=1)

        else:
            messagebox.showwarning(message='Invalid method')

    # Perform function when self.go_button is pressed
    def use_go_button(self):
        curr_method = self.combo.get().lower()

        if curr_method == 'add movie':
            if all([self.entry_title.get(), self.entry_genre.get(), self.entry_platform.get(), self.entry_rent.get()]):
                self.movies.add_movie(self.entry_title.get(),
                                    self.entry_genre.get(),
                                    self.entry_platform.get(),
                                    self.entry_rent.get())
                
                self.entry_title.delete(0, tk.END)
                self.entry_genre.delete(0, tk.END)
                self.entry_platform.delete(0, tk.END)
                self.entry_rent.delete(0, tk.END)
            
            else:
                messagebox.showwarning(message='Please fill all entries')

        elif curr_method == 'true random':
            movie = self.movies.true_random()

            if not movie: messagebox.showwarning(message='Please add movies first')

            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', f"Title: {movie['title']}\nGenre: {movie['genre']}\nPlatform: {movie['platform']}\nRent: {movie['rent']}")
        
        elif curr_method == 'genre random':
            movie = self.movies.genre_random(self.entry_genre.get())

            if not movie: messagebox.showwarning(message='Genre not found')
            
            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', f"Title: {movie['title']}\nGenre: {movie['genre']}\nPlatform: {movie['platform']}\nRent: {movie['rent']}")

        elif curr_method == 'platform random':
            movie = self.movies.platform_random(self.entry_platform.get())

            if not movie: messagebox.showwarning(message='Platform not found')

            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', f"Title: {movie['title']}\nGenre: {movie['genre']}\nPlatform: {movie['platform']}\nRent: {movie['rent']}")

        elif curr_method == 'rent random':
            movie = self.movies.rent_random(self.entry_rent.get())

            if not movie: messagebox.showwarning(message='Rent status not found')

            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', f"Title: {movie['title']}\nGenre: {movie['genre']}\nPlatform: {movie['platform']}\nRent: {movie['rent']}")

        elif curr_method == 'search title':
            movie = self.movies.search_title(self.entry_title.get())

            if not movie: messagebox.showwarning(message='Title not found')

            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', f"Title: {movie['title']}\nGenre: {movie['genre']}\nPlatform: {movie['platform']}\nRent: {movie['rent']}")

        else:
            messagebox.showwarning(message='Invalid method')

    # Saves held movie data into movies.json and closes window
    def save_and_exit(self):
        with open('movies.json', mode = 'w') as movie_w:
            json.dump(self.movies.movie_list, movie_w, indent=4)

        self.root.destroy()
    
    # Removes current movie from held movie data
    def remove_movie2(self):
        # Passes movie title to main remove_movie function in MovieGenerator
        self.movies.remove_movie(self.text.get('1.7', tk.END).split()[0])

        self.text.delete('1.0', tk.END)


class MovieGenerator:
    def __init__(self, movie_list={'movies': []}):
        self.movie_list = movie_list
    

    # Append new movie dict to movie_list
    def add_movie(self, title, genre, platform, rent):
        self.movie_list['movies'].append({'title': title,
                                          'genre': genre,
                                          'platform': platform,
                                          'rent': rent})

    # Find and return movie with relevant title
    def search_title(self, title):
        for movie in self.movie_list['movies']:
            if movie['title'].lower() == title.lower():
                return movie

        return False

    # Return random movie
    def true_random(self):
        if not self.movie_list['movies']: return False

        return choice(self.movie_list['movies']) 
    
    # Creates list of movies if they're specified genre and return random one
    def genre_random(self, genre):
        if not self.movie_list['movies']: return False

        genre_list = [movie for movie in self.movie_list['movies'] if movie['genre'].lower() == genre.lower()]

        if genre_list:
            return choice(genre_list)
        
        else:
            return False

    # Creates list of movies if they're specified platform and return random one
    def platform_random(self, platform):
        if not self.movie_list['movies']: return False

        platform_list = [movie for movie in self.movie_list['movies'] if movie['platform'].lower() == platform.lower()]

        if platform_list:
            return choice(platform_list)
        
        else:
            return False

    # Creates list of movies if they're specified rental status and return random one
    def rent_random(self, rent):
        rent_list = [movie for movie in self.movie_list['movies'] if movie['rent'].lower() == rent.lower()]

        if rent_list:
            return choice(rent_list)
        
        else:
            return False

    # Removes movie from held movie data
    def remove_movie(self, title):
        for movie in self.movie_list['movies']:
            if movie['title'].lower() == title.lower():
                self.movie_list['movies'].remove(movie)


def main():
    root = tk.Tk()
    root.title('Movie Generator')

    window = App(root)

    root.mainloop()

if __name__ == '__main__':
    main()