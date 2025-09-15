# 🎼 Classical Music Creation with Deep Learning

## 📌 프로젝트 개요
이 프로젝트는 **딥러닝 기반 음악 생성 모델**을 활용하여 **클래식 음악(피아노 곡 중심)** 을 자동으로 작곡하는 것을 목표로 합니다.  
RNN 계열 모델(LSTM)을 기반으로 MIDI 데이터를 학습시켜, 새로운 음악 시퀀스를 생성합니다.  

## 🚀 주요 기능
- 대규모 **클래식 음악 MIDI 데이터셋** 학습  
- **LSTM 기반 시퀀스 모델**을 활용한 음악 생성  
- 생성된 결과물은 **MIDI 파일 및 오디오 파일(WAV/MP3)** 로 변환 가능  
- 다양한 시드(Seed) 입력을 통해 **독창적인 멜로디 생성**  


## 📂 데이터셋
- [Aria MIDI Dataset (HuggingFace)](https://huggingface.co/datasets/loubb/aria-midi)  
- 추가 참고: [Kaggle Notebook - Classical Music Generation with LSTM](https://www.kaggle.com/code/melissamonfared/classical-music-generation-lstm/notebook)  

데이터셋 전처리 과정:
1. MIDI → 음표(Notes) 및 코드(Chords) 파싱  
2. 시퀀스 단위로 Tokenization  
3. 모델 입력(X) / 출력(y) 시퀀스 생성  

## 🏗️ 모델 아키텍처
본 프로젝트는 **LSTM(Long Short-Term Memory) 네트워크** 기반으로 설계되었습니다.

- **Embedding Layer**: 음표 시퀀스를 벡터로 매핑  
- **Stacked LSTM Layers**: 시간 의존성을 학습  
- **Dropout Regularization**: 과적합 방지  
- **Dense Layer + Softmax**: 다음 음표 예측  

추가적으로, **Temperature Sampling** 기법을 적용하여 다양한 곡 스타일을 생성할 수 있습니다.  


## ⚙️ 설치 및 실행 방법

### 1️⃣ 환경 세팅
```bash
git clone https://github.com/yourusername/classical-music-creation.git
cd classical-music-creation

# 가상환경 생성
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\\Scripts\\activate      # Windows

# 필수 라이브러리 설치
pip install -r requirements.txt
```

### 2️⃣ 학습 데이터 준비
```bash
# 데이터셋 다운로드 (예시)
wget https://huggingface.co/datasets/loubb/aria-midi -O data/aria-midi
```

### 3️⃣ 모델 학습
```bash
python train.py --epochs 100 --batch_size 64 --save_dir checkpoints/
```

### 4️⃣ 음악 생성
```bash
python generate.py --checkpoint checkpoints/model.h5 --output generated_song.mid
```

## 🎧 데모 결과물
생성된 음악은 아래 링크에서 확인할 수 있습니다:  
- [SoundCloud Demo #1](https://soundcloud.com/be-ngsu/4cc47250-abc6-4bfe-9bbe-0d1250de76e8)  
- [SoundCloud Demo #2](https://soundcloud.com/be-ngsu/f8cff04c-5180-449f-8041-e420c160089e)  
- [SoundCloud Demo #3](https://soundcloud.com/be-ngsu/a237792b-5105-43cf-bf29-d273a7476bb5)  

## 📊 프로젝트 구조
```
classical-music-creation/
│── data/                # MIDI 데이터셋
│── notebooks/           # 실험용 Jupyter 노트북
│── src/                 
│   ├── preprocess.py    # 데이터 전처리
│   ├── model.py         # 모델 정의 (LSTM)
│   ├── train.py         # 학습 스크립트
│   ├── generate.py      # 음악 생성 스크립트
│── checkpoints/         # 학습된 모델 가중치
│── requirements.txt     # 라이브러리 목록
│── README.md
```

## 📌 참고 자료
- [Kaggle Notebook: Classical Music Generation with LSTM](https://www.kaggle.com/code/melissamonfared/classical-music-generation-lstm/notebook)  
- [HuggingFace Dataset: Aria MIDI](https://huggingface.co/datasets/loubb/aria-midi)  
- [SoundCloud Demo Results](https://soundcloud.com/be-ngsu/sets/ai)  