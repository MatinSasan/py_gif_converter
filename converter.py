import os
import imageio

your_input_path = input("enter the name of your video: ")
clip = os.path.abspath(your_input_path)


def gif_maker(input_path, target_format):
    #  ("ed", ".mp4") => "ed.gif"
    output_path = os.path.splitext(input_path)[0] + target_format
    print(f'converting {input_path} \n to {output_path}')

    reader = imageio.get_reader(input_path)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(output_path, fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frame {frames}')

    print('Done!')
    writer.close()


gif_maker(clip, '.gif')
