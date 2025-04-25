# Sistema Embarcado para Detecção de Quedas em Ambientes Residenciais

## Descrição

Este projeto desenvolve um sistema embarcado capaz de **detectar quedas** em ambientes residenciais, especialmente focado em melhorar a **saúde e qualidade de vida de idosos**.  
Utilizando câmeras e processamento de imagem com **microcontroladores Arduino**, o sistema identifica quedas e emite **alertas em tempo real** através de um **buzzer**.

---

## Funcionalidades

- 🎥 Captura de vídeo para monitoramento.
- 🧠 Processamento de imagem com **MediaPipe Pose** para detecção de posições corporais.
- ⚡ Comunicação serial com **Arduino** para acionar alertas.
- 🔔 Emissão de alertas sonoros com **buzzer** quando uma queda é detectada.
- 👵 Aplicação voltada ao cuidado de idosos e melhoria da segurança residencial.

---

## Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [Arduino](https://www.arduino.cc/)
- Comunicação Serial (via biblioteca `pyserial`)

---

## Requisitos

- Python 3 instalado
- Arduino configurado com um buzzer conectado
- Bibliotecas Python:
  ```bash
  pip install opencv-python mediapipe pyserial
  ```
- Porta serial correta configurada no código (`COM5`, `COM3`, etc.)
- Vídeo de entrada (`video.mp4`) para testes

---

## Como Funciona

1. A câmera captura o vídeo do ambiente.
2. O algoritmo identifica a posição dos **ombros** e **quadris** usando o **MediaPipe Pose**.
3. Caso o **ombro** esteja abaixo de um valor limite no eixo Y (indicando possível queda), o sistema inicia uma contagem de frames consecutivos.
4. Se a queda persistir além do limite (`LIMIAR_QUEDA`), o sistema:
   - Envia o sinal para o Arduino (`b'1'` via serial).
   - Aciona o buzzer para alertar.

---

## Execução

1. **Conecte** o Arduino à porta USB.
2. **Compile e carregue** o programa Arduino (com lógica para buzzer).
3. No computador, execute o script Python:

```bash
python detectar_queda.py
```

4. Pressione **'q'** para encerrar o sistema.

---

## Alunos

- **Gustavo Vegi** - RM550188
- **Pedro Henrique Silva de Morais** - RM98804
- **Lucas Rodrigues Delfino** - RM550196
- **Luisa Cristina dos Santos Neves** - RM551889
- **Gabriel Aparecido Cassalho Xavier** - RM99794


