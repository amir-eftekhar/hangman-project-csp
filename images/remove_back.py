from PIL import Image

def remove_background_gif(input_path, output_path, bg_color=(255, 255, 255)):
    img = Image.open(input_path)
    frames = []
    for frame in ImageSequence.Iterator(img):
        rgba = frame.convert("RGBA")
        data = np.array(rgba)
        red, green, blue, alpha = data.T
        white_areas = (red == bg_color[0]) & (green == bg_color[1]) & (blue == bg_color[2])
        data[..., :-1][white_areas.T] = (0, 0, 0)
        data[..., -1][white_areas.T] = 0
        result = Image.fromarray(data)
        frames.append(result)
    frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0)

remove_background_gif('input.gif', 'output.gif')