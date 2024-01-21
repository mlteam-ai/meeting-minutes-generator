import mm_generator

class MainApp:
    def __init__(self, audio_file_path = "Earningscall.wav", output_file_name="meeting_minutes.docx") -> None:
        self.mm_generator = mm_generator.MeetingMinutesGenerator()
        self.audio_file_path = audio_file_path
        self.output_file_name = output_file_name
    
    def run(self):
        transcription = self.mm_generator.transcribe_audio(self.audio_file_path)
        minutes = self.mm_generator.meeting_minutes(transcription)
        print(minutes)
        self.mm_generator.save_as_docx(minutes, self.output_file_name)

if __name__ == "__main__":
    app = MainApp()
    app.run()