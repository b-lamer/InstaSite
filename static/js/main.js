let instaLoader = null;

async function login() {
    const username = document.getElementById('loginUsername').value.trim();
    const password = document.getElementById('loginPassword').value.trim();
    const statusDiv = document.getElementById('loginStatus');
    
    if (!username || !password) {
        showStatusMessage('Please enter both username and password', false);
        return;
    }

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();
        
        if (response.ok) {
            showStatusMessage('Login successful!', true);
            document.getElementById('loginSection').classList.add('hidden');
            document.getElementById('checkerSection').classList.remove('hidden');
        } else {
            showStatusMessage(data.error || 'Login failed', false);
        }
    } catch (error) {
        showStatusMessage('Failed to connect to server', false);
    }
}

function logout() {
    fetch('/logout', { method: 'POST' })
        .then(() => {
            document.getElementById('loginSection').classList.remove('hidden');
            document.getElementById('checkerSection').classList.add('hidden');
            document.getElementById('loginUsername').value = '';
            document.getElementById('loginPassword').value = '';
            document.getElementById('loginStatus').innerHTML = '';
        });
}

function showStatusMessage(message, isSuccess) {
    const statusDiv = document.getElementById('loginStatus');
    statusDiv.innerHTML = message;
    statusDiv.className = 'status-message ' + (isSuccess ? 'success' : 'error');
}

async function checkFollowers() {
    const username = document.getElementById('username').value.trim();
    const resultDiv = document.getElementById('result');
    const loader = document.getElementById('loader');
    
    if (!username) {
        showError('Please enter a username');
        return;
    }

    loader.style.display = 'block';
    resultDiv.innerHTML = '';
    
    try {
        const response = await fetch('/instagram', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username: username })
        });

        const data = await response.json();
        
        if (response.ok) {
            displayResults(data.badfriends);
        } else {
            showError(data.error || 'An error occurred');
        }
    } catch (error) {
        showError('Failed to fetch data. Please try again.');
    } finally {
        loader.style.display = 'none';
    }
}

function displayResults(badfriends) {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';

    if (!badfriends || badfriends.length === 0) {
        resultDiv.innerHTML = '<div class="result-item">Everyone is following you back! 🎉</div>';
        return;
    }

    badfriends.forEach(username => {
        const userDiv = document.createElement('div');
        userDiv.className = 'result-item';
        userDiv.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
            </svg>
            ${username}
        `;
        resultDiv.appendChild(userDiv);
    });
}

function showError(message) {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `<div class="error-message">${message}</div>`;
}
