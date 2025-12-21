/* ==========================================================================
   DOM読み込み完了後の処理
   ========================================================================== */
document.addEventListener('DOMContentLoaded', () => {
    
    // ----------------------------------------------------------------------
    // 1. Lucideアイコンの初期化
    // ----------------------------------------------------------------------
    // <i data-lucide="..."></i> タグをSVGアイコンに変換します
    lucide.createIcons();


    // ----------------------------------------------------------------------
    // 2. スクロール時の「ふわっと表示」アニメーション制御
    // ----------------------------------------------------------------------
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1 // 画面の10%が見えたら発火
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // 画面内に入ったら 'is-visible' クラスを付与
                entry.target.classList.add('is-visible');
                // 一度表示したら監視を終了（負荷軽減のため）
                observer.unobserve(entry.target); 
            }
        });
    }, observerOptions);

    // .fade-in-section クラスがついている要素をすべて監視対象にする
    const sections = document.querySelectorAll('.fade-in-section');
    sections.forEach(section => {
        observer.observe(section);
    });


    // ----------------------------------------------------------------------
    // 3. 古物商プレートの拡大表示モーダル制御
    // ----------------------------------------------------------------------
    const modal = document.getElementById('js-license-modal');
    const trigger = document.getElementById('js-license-trigger');
    const closeBtn = document.getElementById('js-modal-close');
    const overlay = document.getElementById('js-modal-overlay');

    // モーダルを表示する関数
    const openModal = () => {
        modal.classList.remove('hidden'); // まずdisplay:noneを解除
        // 少し遅らせてopacityを1にすることでフェードインさせる
        setTimeout(() => {
            modal.classList.add('is-open');
        }, 10);
    };

    // モーダルを閉じる関数
    const closeModal = () => {
        modal.classList.remove('is-open'); // フェードアウト
        // トランジションが終わった頃に非表示にする
        setTimeout(() => {
            modal.classList.add('hidden');
        }, 300); // CSSのduration-300に合わせる
    };

    // イベントリスナーの設定
    if (trigger && modal) {
        // 画像クリックで開く
        trigger.addEventListener('click', (e) => {
            e.preventDefault();
            openModal();
        });

        // 閉じるボタンで閉じる
        closeBtn.addEventListener('click', closeModal);
        
        // 背景（オーバーレイ）クリックで閉じる
        overlay.addEventListener('click', closeModal);
    }

    // ----------------------------------------------------------------------
    // 4. スマホメニューの開閉制御
    // ----------------------------------------------------------------------
    const menuBtn = document.getElementById('js-menu-btn');
    const mobileMenu = document.getElementById('js-mobile-menu');
    const mobileLinks = document.querySelectorAll('.js-mobile-link');
    const iconMenu = document.getElementById('js-icon-menu');
    const iconClose = document.getElementById('js-icon-close');

    if (menuBtn && mobileMenu) {
        // ボタンクリックでメニューの表示/非表示を切り替え
        menuBtn.addEventListener('click', () => {
            // メニューの表示切り替え
            mobileMenu.classList.toggle('hidden');
            
            // アイコンの切り替え
            if (iconMenu && iconClose) {
                iconMenu.classList.toggle('hidden');
                iconClose.classList.toggle('hidden');
            }
        });

        // メニュー内のリンクをクリックしたらメニューを閉じる
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                // アイコンを初期状態（メニュー）に戻す
                if (iconMenu && iconClose) {
                    iconMenu.classList.remove('hidden');
                    iconClose.classList.add('hidden');
                }
            });
        });
    }
});