import numpy as np
import wave

def read_wave_file(filename):
    """Lê os dados de áudio de um arquivo WAV."""
    with wave.open(filename, 'rb') as wf:
        sample_rate = wf.getframerate()
        num_frames = wf.getnframes()
        audio_data = wf.readframes(num_frames)
        audio_data = np.frombuffer(audio_data, dtype=np.int16)
    return audio_data, sample_rate

def decode_zx_spectrum_audio(audio_data, sample_rate):
    """Decodifica o áudio ZX Spectrum em dados binários."""
    pulse_0_length = int(sample_rate / 1000)  # Duração do pulso para '0' em samples
    pulse_1_length = int(sample_rate / 500)   # Duração do pulso para '1' em samples

    bitstream = []
    i = 0
    while i < len(audio_data):
        # Verificar se estamos em um pulso
        if audio_data[i] > 0.5:
            # Verificar o comprimento do pulso
            pulse_length = 1
            while i + pulse_length < len(audio_data) and audio_data[i + pulse_length] > 0.5:
                pulse_length += 1
            
            if pulse_length >= pulse_1_length:
                bitstream.append('1')
            else:
                bitstream.append('0')
            
            # Pular a duração do pulso e a pausa entre pulsos
            i += pulse_length + pulse_0_length
        else:
            i += 1
    
    return ''.join(bitstream)

def binary_to_text(binary_data):
    """Converte dados binários em texto."""
    chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return ''.join(chars)

def main():
    # Solicita o nome do arquivo WAV ao usuário
    filename = input("Digite o nome do arquivo WAV: ")

    # Lê o arquivo WAV
    audio_data, sample_rate = read_wave_file(filename)
    
    # Decodifica o áudio para dados binários
    binary_data = decode_zx_spectrum_audio(audio_data, sample_rate)
    
    # Converte os dados binários para texto
    text = binary_to_text(binary_data)
    
    # Exibe o texto no console
    print("Conteúdo do arquivo de texto:")
    print(text)
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    main()



