import ollama 

# create streaming completion 
completion = ollama.chat(
    model='deepseek-r1:8b',
    messages=[
        {'role': 'system', 'content': 'you are a helpfull assistant.'},
        {'role': 'user', 'content': 'why sky is blue?'}
    ],
)

# ACESS MESSAGE CONTENT DIRECTLY FROM RESPONSE 
response = completion['message']['content']

print(response)


# output 
'''                                                                                        
<think>
Okay, so I'm trying to figure out why the sky appears blue. From what I know, when light hits an object like water or ground, it reflects off the surface. But how does that make it look blue?

I remember that blue light has a shorter wavelength than red and green light. So maybe the reason is about different wavelengths. Water molecules are small, so maybe they allow blue to pass through while letting longer wavelengths go out of view. That could make the sky appear blue because we're seeing more of the shorter wavelengths.

But wait, there's also something called Rayleigh scattering. I think that's a process where light interacts with particles in the air and gets scattered. For visible light, the particles are much bigger than in water or soil, right? So maybe that's why Rayleigh scattering doesn't affect longer wavelengths as much, making blue appear more.

I'm also thinking about how colors come from different parts of the spectrum. When sunlight enters Earth, it has all the colors, but each color is absorbed by objects at certain temperatures. Like plants absorb green light when they grow, so we see them through that.

So maybe when the sky reflects off particles in the air and water, those smaller particles allow blue to pass through more than other colors. That would make the sky appear blue because more of the blue is visible compared to the red or green from Rayleigh scattering.

I'm not entirely sure if I'm mixing up Rayleigh scattering with something else, but I think that's part of why the sky looks blue. There might be other factors like Earth's magnetic field causing sunlight to scatter differently, but the main reason seems to be about particle size and absorption.
</think>

The appearance of the sky as blue is primarily due to two key processes:

1. **Rayleigh Scattering**: This affects visible light by allowing shorter wavelengths (blue) to pass through while longer wavelengths (red, green) are scattered out of view. Smaller particles in the air, such as water molecules, enable this effect.

2. **Color Emission from Earth**: Plants and other organisms emit light at specific wavelengths corresponding to their colors. For example, plants emit green light when they grow because they absorb blue and red light due to Rayleigh scattering.

These processes together create a mix of visible colors, with more of the blue being reflected back into our atmosphere by water molecules in the sky.

'''