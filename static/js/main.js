// ===========================
// SHEOZY - Main JavaScript
// ===========================

document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initializeScrollAnimations();
    initializeMessages();
    updateCartCount();
});

// ===========================
// Scroll Animations
// ===========================

function initializeScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animationDelay = '0.2s';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });
}

// ===========================
// Messages Auto-Hide
// ===========================

function initializeMessages() {
    const messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        const closeBtn = message.querySelector('.close');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                message.style.animation = 'slideOutRight 0.3s ease-out forwards';
                setTimeout(() => message.remove(), 300);
            });
        }

        // Auto-hide after 5 seconds
        setTimeout(() => {
            if (message.parentElement) {
                message.style.animation = 'slideOutRight 0.3s ease-out forwards';
                setTimeout(() => message.remove(), 300);
            }
        }, 5000);
    });
}

// ===========================
// Cart Functions
// ===========================

function updateCartCount() {
    const cartCount = localStorage.getItem('cart-count') || '0';
    const cartElement = document.getElementById('cart-count');
    if (cartElement) {
        cartElement.textContent = cartCount;
    }
}

function addToCartAjax(productId, quantity = 1) {
    const form = new FormData();
    form.append('quantity', quantity);
    form.append('csrfmiddlewaretoken', getCookie('csrftoken'));

    fetch(`/api/cart/add/${productId}/`, {
        method: 'POST',
        body: form,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            updateCartCount();
            showNotification('Added to cart!', 'success');
            // Update cart count display
            const cartCountElement = document.getElementById('cart-count');
            if (cartCountElement) {
                cartCountElement.textContent = data.total_items;
            }

            if (data.redirect_url) {
                window.location.href = data.redirect_url;
                return;
            }
        } else {
            showNotification(data.message || 'Error adding to cart', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Error adding to cart', 'error');
    });
}

// ===========================
// Utilities
// ===========================

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function showNotification(message, type = 'info') {
    const messagesContainer = document.querySelector('.messages') || createMessagesContainer();
    const alert = document.createElement('div');
    alert.className = `alert alert-${type} animate-in`;
    alert.innerHTML = `
        ${message}
        <button class="close">&times;</button>
    `;

    messagesContainer.appendChild(alert);

    const closeBtn = alert.querySelector('.close');
    closeBtn.addEventListener('click', function() {
        alert.style.animation = 'slideOutRight 0.3s ease-out forwards';
        setTimeout(() => alert.remove(), 300);
    });

    setTimeout(() => {
        if (alert.parentElement) {
            alert.style.animation = 'slideOutRight 0.3s ease-out forwards';
            setTimeout(() => alert.remove(), 300);
        }
    }, 5000);
}

function createMessagesContainer() {
    const container = document.createElement('div');
    container.className = 'messages';
    document.body.appendChild(container);
    return container;
}

// ===========================
// Image Lazy Loading
// ===========================

document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
});

// ===========================
// Smooth Scrolling
// ===========================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});
