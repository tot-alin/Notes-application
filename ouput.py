from fpdf import FPDF
from gtts import gTTS
from playsound3 import playsound
import os


class ExportPdfDoc:

    @staticmethod
    def export_to_pdf(notes_title_in, notes_in):
        doc_pdf = FPDF(orientation='P', unit='mm', format='A4')
        doc_pdf.set_auto_page_break(True, 25)  # marginea de jos 25
        doc_pdf.set_margins(left=25, top=20)
        doc_pdf.add_page()
        doc_pdf.add_font("Arial", '', 'arial.ttf', True)
        doc_pdf.set_font("Arial", size=12)
        # creaza celule
        doc_pdf.cell(160, 10, txt=notes_title_in, ln=1, align='C')
        doc_pdf.multi_cell(160, 10, txt=notes_in, align='L') # .encode('utf-8').decode('latin-1')
        # salveaza
        doc_pdf.output('notes.pdf')
        #   messagebox.showinfo(message='PDF is ready', parent=frame_note)

class Audio:

    @staticmethod
    def create_sound(text, lang_set):
        try:
            tts = gTTS(text=text, lang=lang_set)
            tts.save('temp.wav')
            Audio.play()
        except:
            print('Error in gTTS')
            pass
        os.remove('temp.wav')

    @staticmethod
    def play():
        try:
            playsound('temp.wav')
        except:
            print('Error in playsound')
            pass
