import http.server
import json
import os
import subprocess
import zipfile
import time
import random

# --- BASE DE DATOS ENCICLOPÉDICA NIVEL 4 ---

GENRES = [
    {"name": "Melodic Techno", "artists": "Tale Of Us, Anyma", "bpm": (122, 126), "key_pool": ["F minor", "G minor", "A minor"], "vibe": "Pads cinemáticos, reverb inmensa"},
    {"name": "Afro House", "artists": "Keinemusik, Black Coffee", "bpm": (118, 122), "key_pool": ["D minor", "C minor", "F# minor"], "vibe": "Percusiones orgánicas, shakers, bajo melódico"},
    {"name": "Tech House", "artists": "John Summit, Fisher", "bpm": (126, 128), "key_pool": ["A minor", "E minor", "G minor"], "vibe": "Bajo funk con glide, build-ups ruidosos"},
    {"name": "UK Garage / 2-Step", "artists": "Fred again.., Interplanetary Criminal", "bpm": (130, 138), "key_pool": ["F# minor", "B minor"], "vibe": "Chops vocales, ritmo 2-step glitcheado"},
    {"name": "Drum & Bass", "artists": "Noisia, Dimension", "bpm": (170, 175), "key_pool": ["E minor", "F minor"], "vibe": "Diseño de graves extremos, breaks granulados"}
]

KICK_EQ = ["Pultec EQP-1A (Boost & Attenuate 30Hz)", "SSL 4000 E-Channel (Scoop en 250Hz)", "FabFilter Pro-Q 3 (Dynamic EQ, -3dB en 150Hz)", "Maag EQ4 (Sub Band active)"]
BASS_COMP = ["1176 FET (Ataque ultra rápido, ratio 4:1)", "LA-2A Opto (Compresión suave, 2-3dB GR)", "Distorsión FabFilter Saturn 2 multibanda", "Saturación Soundtoys Decapitator (Modo E)"]
SYNTH_GEAR = ["Serum (Wavetable + FM)", "Diva (Analógico Modelado tipo Minimoog)", "Vital (Modulación Espectral)", "Operator (FM de 4 operadores)", "Omnisphere (Síntesis Granular)"]
VOCAL_PROC = ["De-Essing en 7kHz + OTT agresivo", "Cadena serial: 1176 (Picos) -> LA-2A (Nivelación)", "Valhalla VintageVerb (Modo 1970s)", "Reverb Lexicon 480L (Random Hall)"]
PERC_PROC = ["Distorsión de cinta Kramer Tape (15 ips)", "Compresión de Bus SSL G-Bus (Ratio 2:1)", "Echoboy Delay (Ping-Pong a 1/8)", "Saturación Klanghelm SDRR (Modo Desk)"]

DRUM_MACHINES = ["Roland TR-909", "Roland TR-808", "LinnDrum", "Akai MPC60 (12-bit swing)"]

def generate_mock_json(input_target, daw, mode="D2", breakdown="all"):
    title = f"{input_target}"
    
    if input_target.startswith("http"):
        try:
            result = subprocess.run(
                ["yt-dlp", "--get-title", input_target],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0 and result.stdout.strip():
                title = result.stdout.strip()
        except Exception:
            pass

    
    # Seleccionamos un perfil aleatorio basado en la base de datos
    profile = random.choice(GENRES)
    bpm = random.randint(profile["bpm"][0], profile["bpm"][1])
    key = random.choice(profile["key_pool"])
    
    kick_eq = random.choice(KICK_EQ)
    bass_comp = random.choice(BASS_COMP)
    synth = random.choice(SYNTH_GEAR)
    vocal = random.choice(VOCAL_PROC)
    perc = random.choice(PERC_PROC)
    drum_m = random.choice(DRUM_MACHINES)

    track_kick = f"KICK/SUB: Frecuencia detectada 45-50Hz. Modelado de impacto estilo {drum_m}. EQ forense: {kick_eq}. Alineación de fase perfecta con el bajo."
    track_bass = f"BASSLINE: Transitorios definidos. Procesamiento: {bass_comp}. Sidechain pumping detectado (trigger externo de 1/4 note, release 40ms)."
    track_synth = f"SYNTHS/LEADS: Origen sónico inferido: {synth}. Corte LPF automatizado. Ensanchamiento estéreo mediante Efecto Haas."
    track_vocal = f"VOCALS: Chops o voz principal con inteligibilidad máxima en 3kHz. Procesamiento: {vocal}. EQ Mid/Side aislando frecuencias centrales."
    track_perc = f"PERCUSSIONS/TOPS: Hi-hats asimétricos con micro-swing humano (estilo MPC/Groove Pool). Tratamiento: {perc}. Soft-clipping en picos."
    track_fx = "FX/ATMOSPHERES: Barridos de ruido blanco (24dB/oct LPF). Impactos sub-graves con pre-delay de 30ms en la reverb para mantener claridad."

    tracks = [track_kick, track_bass, track_synth, track_vocal, track_perc, track_fx]

    if breakdown == "rhythm":
        tracks = [track_kick, track_perc, track_bass]
    elif breakdown == "melodic":
        tracks = [track_synth, track_vocal, track_fx]
    elif breakdown == "lowend":
        tracks = [track_kick, track_bass]

    if mode == "D1":
        consejo = "Extracción D1: Transitorios y Groove. Pistas mapeadas con el swing detectado. Cuantiza al 60% para replicar el feel de la pista."
    elif mode == "D2":
        consejo = "Extracción D2: Polifonía y Stemming Profundo. Revisa la ecualización Mid/Side en los buses de síntesis para lograr la misma amplitud."
    elif mode == "D3":
        consejo = "Extracción D3 Forense: Curva de Masterización clonada. Aplica iZotope Ozone o FabFilter Pro-L 2 con Lookahead a 1ms y True Peak -0.1dB."
    else:
        consejo = "Aplica compresión paralela agresiva estilo New York."

    zip_filename = f"AlienBox_{daw}_{int(time.time())}.zip"
    zip_path = os.path.join(os.getcwd(), zip_filename)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.writestr("Info.txt", f"Alien Box Extracted Project\\nTrack: {title}\\nDAW: {daw}\\nBPM: {bpm}\\nKey: {key}\\nMode: {mode}\\nBreakdown: {breakdown}\\n")
        zipf.writestr("MIDI/Kick.mid", "MThd... dummy")
        zipf.writestr("MIDI/Bass.mid", "MThd... dummy")
        zipf.writestr(f"Template/{daw}_Template.xml", "<project>Dummy</project>")
        
    download_url = f"http://localhost:8000/{zip_filename}"

    mock_data = {
        "status": "success",
        "ficha_tecnica": {
            "titulo": title,
            "genero": f"{profile['name']} (Estilo: {profile['artists']})",
            "bpm": bpm,
            "tonalidad": key,
            "rango_dinamico": f"-{random.randint(6, 9)}.5 LUFS (Estándar de Club)",
            "fase_estereo": "Correlación +0.65 (Sub-graves 100% Mono < 120Hz)",
            "estructura": [
                "0:00 - 0:32 (Intro: Filtro paso-bajo automatizado, percusión orgánica)",
                "0:32 - 1:04 (Pre-Drop: Silencio súbito de 1 tiempo, snare roll creciente)",
                "1:04 - 1:36 (Drop: Máxima energía, subgrave FM y Kick estables)",
                "1:36 - 2:08 (Breakdown: Vocales procesadas con reverb enorme infinita)"
            ]
        },
        "midi_data": {
            "mode": mode,
            "breakdown": breakdown,
            "tracks": tracks
        },
        "guia_verificacion": f"Técnicas Masterización Detectadas:\\n- Limitación Brickwall Transparente (Target: LUFS agresivo).\\n- EQ de Mastering en sonrisa (Smile Curve SSL).\\n- Uso intensivo de saturación armónica ({random.choice(BASS_COMP)}) en el Drum Bus.",
        "consejo_productor": consejo,
        "plantilla_zip_url": download_url
    }
    return mock_data

class AlienBoxHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

    def do_POST(self):
        if self.path == '/alienbox':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            data = json.loads(post_data.decode('utf-8'))
            input_target = data.get('input', 'Unknown Track')
            daw = data.get('daw', 'Ableton')
            mode = data.get('mode', 'D2')
            breakdown = data.get('breakdown', 'all')
            
            print(f"[ALIEN ENGINE] Auditoría Forense: {input_target} | {daw} | Modo: {mode} | Foco: {breakdown}")
            
            response_json = generate_mock_json(input_target, daw, mode, breakdown)
            
            if mode == "D1":
                time.sleep(1)
            elif mode == "D2":
                time.sleep(2)
            elif mode == "D3":
                time.sleep(3)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_json).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, AlienBoxHandler)
    print("AlienBox Backend Server Forense (Nivel 4) corriendo en puerto 8000...")
    httpd.serve_forever()
