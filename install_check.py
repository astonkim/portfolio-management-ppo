import sys
print(f"Python: {sys.version}")
print(f"현재 작업 디렉토리: {sys.path[0]}")

libraries = {
    'numpy': 'NumPy',
    'pandas': 'Pandas', 
    'torch': 'PyTorch',
    'stable_baselines3': 'Stable-Baselines3',
    'gymnasium': 'Gymnasium',
    'sklearn': 'Scikit-learn',
    'matplotlib': 'Matplotlib',
    'yfinance': 'yfinance',
    'finrl': 'FinRL'
}

print("\n=== 라이브러리 설치 상태 ===")
for lib, name in libraries.items():
    try:
        module = __import__(lib)
        version = getattr(module, '__version__', 'Unknown')
        print(f"✅ {name}: {version}")
    except ImportError as e:
        print(f"❌ {name}: 설치되지 않음")

# PyTorch 디바이스 확인
print(f"\n=== PyTorch 환경 ===")
try:
    import torch
    print(f"   - PyTorch 버전: {torch.__version__}")
    print(f"   - MPS 사용 가능: {torch.backends.mps.is_available()}")
    print(f"   - CPU 코어 수: {torch.get_num_threads()}")
    
    # 간단한 텐서 연산 테스트
    x = torch.randn(10, 10)
    y = torch.mm(x, x.t())
    print(f"   - 텐서 연산 테스트: ✅ 성공")
except Exception as e:
    print(f"   - PyTorch 테스트 실패: {e}")

# FinRL 세부 테스트
print(f"\n=== FinRL 세부 기능 테스트 ===")
try:
    # 핵심 모듈들 개별 테스트
    from finrl.meta.preprocessor.yahoodownloader import YahooDownloader
    print("✅ YahooDownloader 사용 가능")
except ImportError as e:
    print(f"❌ YahooDownloader: {e}")

try:
    from finrl.meta.env_stock_trading.env_stocktrading import StockTradingEnv
    print("✅ StockTradingEnv 사용 가능")
except ImportError as e:
    print(f"❌ StockTradingEnv: {e}")

try:
    import pandas_market_calendars
    print("✅ pandas_market_calendars 사용 가능")
except ImportError as e:
    print(f"❌ pandas_market_calendars: {e}")

print(f"\n=== 환경 설정 완료 상태 ===")
print("연구 환경이 준비되었습니다! 🚀")
