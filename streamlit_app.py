import streamlit as st
from textwrap import dedent


st.set_page_config(
    page_title="한소윤 | 자기소개",
    page_icon="🐱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.html(
    dedent("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Jua&display=swap');

    :root {
        --ink: #173d5b;
        --muted: #52718a;
        --blue: #5da9e9;
        --line: rgba(50, 109, 157, 0.16);
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(145deg, #eff9ff 0%, #dcefff 48%, #f3f8ff 100%);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1100px;
        padding: 2.5rem 2rem 3rem;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .profile-page {
        color: var(--ink);
        font-family: 'Gowun Dodum', 'Malgun Gothic', sans-serif;
    }

    .hero {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 2rem;
        min-height: 365px;
        overflow: hidden;
        padding: clamp(2rem, 6vw, 4.5rem);
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 24px;
        background: linear-gradient(120deg, rgba(255,255,255,.9), rgba(221,240,255,.78));
        box-shadow: 0 18px 55px rgba(59, 126, 177, 0.11);
    }

    .hero::after {
        position: absolute;
        right: -95px;
        bottom: -180px;
        width: 390px;
        height: 390px;
        border: 1px solid rgba(93, 169, 233, 0.2);
        border-radius: 50%;
        content: '';
    }

    .hero-copy, .hero-art {
        position: relative;
        z-index: 1;
    }

    .eyebrow {
        display: inline-block;
        margin-bottom: 1.1rem;
        padding: .45rem .85rem;
        border: 1px solid #c9e6fb;
        border-radius: 999px;
        background: #f5fbff;
        color: #397eaf;
        font-size: .82rem;
        font-weight: 700;
    }

    .hero h1 {
        margin: 0;
        color: var(--ink);
        font-family: 'Jua', 'Malgun Gothic', sans-serif;
        font-size: clamp(2.25rem, 5vw, 4rem);
        font-weight: 400;
        line-height: 1.25;
    }

    .hero h1 strong {
        color: #378bd0;
        font-weight: 400;
    }

    .hero-copy p {
        max-width: 520px;
        margin: 1.15rem 0 0;
        color: var(--muted);
        font-size: 1.08rem;
        line-height: 1.8;
    }

    .hero-art {
        display: grid;
        width: 210px;
        height: 210px;
        flex: 0 0 210px;
        place-items: center;
        border: 1px solid rgba(255,255,255,.9);
        border-radius: 50%;
        background: radial-gradient(circle at 35% 30%, #fff 0, #edf8ff 48%, #cce8ff 100%);
        box-shadow: 0 15px 38px rgba(69, 142, 196, .15);
        font-size: 5.5rem;
        animation: float 4s ease-in-out infinite;
    }

    .hero-art span {
        transform: translateY(-3px);
    }

    .section {
        margin-top: 3.5rem;
    }

    .section-kicker {
        margin: 0 0 .45rem;
        color: #4b94ca;
        font-size: .82rem;
        font-weight: 700;
    }

    .section h2 {
        margin: 0;
        color: var(--ink);
        font-family: 'Jua', 'Malgun Gothic', sans-serif;
        font-size: 1.8rem;
        font-weight: 400;
    }

    .section-lead {
        margin: .8rem 0 0;
        color: var(--muted);
        line-height: 1.8;
    }

    .facts {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.2rem;
        margin-top: 1.6rem;
    }

    .fact {
        padding: 1.15rem 0;
        border-top: 2px solid #93c9ef;
    }

    .fact-label {
        display: block;
        margin-bottom: .5rem;
        color: #64839b;
        font-size: .88rem;
    }

    .fact-value {
        color: var(--ink);
        font-size: 1.12rem;
        font-weight: 700;
    }

    .interests {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-top: 1.5rem;
    }

    .interest {
        min-height: 145px;
        padding: 1.4rem 1.5rem;
        border: 1px solid rgba(255,255,255,.9);
        border-radius: 12px;
        background: rgba(255,255,255,.58);
    }

    .interest h3 {
        margin: .55rem 0 .35rem;
        color: var(--ink);
        font-size: 1.08rem;
    }

    .interest p {
        margin: 0;
        color: var(--muted);
        line-height: 1.7;
    }

    .note {
        margin-top: 3.5rem;
        padding: 1.5rem 1.75rem;
        border-left: 4px solid #73b8eb;
        background: rgba(255,255,255,.48);
        color: #426984;
        line-height: 1.8;
    }

    .note strong {
        color: #2879b5;
    }

    .page-footer {
        margin-top: 2.5rem;
        color: #7390a5;
        font-size: .85rem;
        text-align: center;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-9px); }
    }

    @media (max-width: 680px) {
        [data-testid="stMainBlockContainer"] {
            padding: 1rem 1rem 2rem;
        }

        .hero {
            min-height: 0;
            flex-direction: column-reverse;
            align-items: flex-start;
            gap: 1.25rem;
            padding: 1.6rem;
            border-radius: 18px;
        }

        .hero-art {
            width: 112px;
            height: 112px;
            flex-basis: 112px;
            align-self: center;
            font-size: 3.3rem;
        }

        .hero-copy p {
            font-size: 1rem;
        }

        .facts {
            grid-template-columns: 1fr;
            gap: .2rem;
        }

        .fact {
            padding: .85rem 0;
        }

        .interests {
            grid-template-columns: 1fr;
        }
    }
    </style>

    <main class="profile-page">
        <section class="hero">
            <div class="hero-copy">
                <span class="eyebrow">SOYOON'S PROFILE · 반가워요!</span>
                <h1>안녕하세요,<br><strong>한소윤</strong>입니다!</h1>
                <p>경복비즈니스고등학교 IT과 3학년 한소윤입니다.<br>관심 있는 분야를 배우며 한 걸음씩 성장하고 있어요.</p>
            </div>
            <div class="hero-art" aria-label="고양이 이모티콘">
                <span>🐱</span>
            </div>
        </section>

        <section class="section">
            <p class="section-kicker">ABOUT ME</p>
            <h2>저를 소개해요</h2>
            <p class="section-lead">새로운 것을 배우고 직접 경험하면서, 저만의 가능성을 넓혀가고 싶습니다.</p>
            <div class="facts">
                <div class="fact">
                    <span class="fact-label">학교</span>
                    <span class="fact-value">경복비즈니스고등학교</span>
                </div>
                <div class="fact">
                    <span class="fact-label">학년 · 전공</span>
                    <span class="fact-value">3학년 · IT과</span>
                </div>
                <div class="fact">
                    <span class="fact-label">이름</span>
                    <span class="fact-value">한소윤</span>
                </div>
            </div>
        </section>

        <section class="section">
            <p class="section-kicker">MY FAVORITES &amp; DREAM</p>
            <h2>좋아하는 것과 꿈꾸는 미래</h2>
            <div class="interests">
                <article class="interest">
                    <h3>취미는 자전거 타기</h3>
                    <p>바람을 느끼며 자전거를 타는 시간이 좋아요. 페달을 밟듯 꾸준히 앞으로 나아가고 싶어요!</p>
                </article>
                <article class="interest">
                    <h3>IT 분야에서 일하기</h3>
                    <p>IT 분야 기업에 취업해 배운 것을 실무에 활용하고, 계속 성장하는 것이 제 목표예요.</p>
                </article>
            </div>
        </section>

        <aside class="note">
            <strong>천천히, 하지만 꾸준히</strong><br>
            오늘의 배움과 경험을 차곡차곡 쌓아서, 제가 꿈꾸는 미래에 한 발씩 다가가겠습니다.
        </aside>

        <p class="page-footer">소윤의 페이지에 들러주셔서 감사합니다</p>
    </main>
    """),
)