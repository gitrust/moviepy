import moviepy.editor as mpy

roles = ["Batman", "Gandalf", "Han Solo", "Luke"]
clips = [ mpy.TextClip(txt, fontsize=70, font='DejaVu-Serif', color='red', size=(600,400))
            .set_duration(2)
          for txt in  roles]
concat_clip = mpy.concatenate_videoclips(clips)
concat_clip.write_videofile("text.mp4",fps=24)
