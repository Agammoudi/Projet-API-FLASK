from openai import OpenAI
import customtkinter
import requests

client = OpenAI(api_key="API_KEY")

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

class requestsAPP(customtkinter.CTk):
    
    user_input = ""
    consigne = ""
    historique_conversation = [{'role': 'system', 'content': ''}]
   
    def __init__(self):
        super().__init__()
        self.title("Mon application #1")
        self.geometry(f"{1100}x{580}")
        
        # Créer une grille de 3 lignes et 3 colonnes
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
    
        # Partie bouton
        self.buton_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.buton_frame.grid(row=0, column=1)
        
        self.button = customtkinter.CTkButton(master=self.buton_frame, text="send", command=self.update_user_input)
        self.button.grid(pady=10)

        self.reset_button = customtkinter.CTkButton(master=self.buton_frame, text="Remise à zéro", command=self.reset_text)
        self.reset_button.grid(pady=10)
        
        # Partie champs texte
        self.text_frame = customtkinter.CTkFrame(self, width=800, corner_radius=0)
        self.text_frame.grid(row=0, column=0)
        
        self.user_text = customtkinter.CTkEntry(master=self.text_frame, height=10, width=800)
        self.user_text.grid(pady=10)
        
        # Nouveau champ pour la consigne
        self.consigne_text = customtkinter.CTkEntry(master=self.text_frame, height=10, width=800, placeholder_text="Entrez la consigne ici")
        self.consigne_text.grid(pady=10)
        
        # Partie résultat
        self.result_frame = customtkinter.CTkFrame(self, width=8000, corner_radius=0)
        self.result_frame.grid(row=1, column=0)
        
        self.result_box = customtkinter.CTkTextbox(master=self.result_frame, height=400, width=800)
        self.result_box.configure(state="disabled")
        self.result_box.grid(sticky="nsew")
        
        # Partie slider de température
        self.slider_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.slider_frame.grid(row=2, column=1)
        
        self.temperature_slider = customtkinter.CTkSlider(master=self.slider_frame, from_=0.0, to=1.0, number_of_steps=100, width=160)
        self.temperature_slider.set(0.5)
        self.temperature_slider.grid(pady=10)
        
        self.temperature_label = customtkinter.CTkLabel(master=self.slider_frame, text=f'Température: {self.temperature_slider.get():.2f}')
        self.temperature_label.grid(pady=5)
        
        self.temperature_slider.bind("<Motion>", self.update_temperature_label)
       
    def update_temperature_label(self, event=None):
        self.temperature_label.configure(text=f'Température: {self.temperature_slider.get():.2f}')

    def update_user_input(self):
        # Récupérer le texte de l'utilisateur
        self.user_input = self.user_text.get()
        
        # Récupérer la consigne de l'utilisateur
        self.consigne = self.consigne_text.get()
        
        # Mettre à jour l'historique de conversation avec la nouvelle consigne
        self.historique_conversation = [{'role': 'system', 'content': self.consigne}]
        self.historique_conversation.append({'role': 'user', 'content': self.user_input})
        print(self.historique_conversation)
        
        # Appeler l'API OpenAI
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.historique_conversation,
                temperature=self.temperature_slider.get()  
            )
            response = completion.choices[0].message.content
            self.historique_conversation.append({'role': 'assistant', 'content': response})
            self.result_box.configure(state="normal")
            self.result_box.insert("end", f'Moi : {self.user_input}\nOpenAI : {response}\n\n')
            self.result_box.configure(state="disabled")
            print(response)
        except Exception as e:
            print(e)
            self.result_box.configure(state="normal")
            self.result_box.insert("end", "Erreur lors de la requête\n")
            self.result_box.configure(state="disabled")
    
    def reset_text(self):
        self.user_text.delete(0, 'end')
        self.consigne_text.delete(0, 'end')
        self.result_box.configure(state="normal")
        self.result_box.delete(1.0, 'end')
        self.result_box.configure(state="disabled")
        self.historique_conversation = [{'role': 'system', 'content': ''}]
        

if __name__ == "__main__":
    mon_instance = requestsAPP()    
    mon_instance.mainloop()
