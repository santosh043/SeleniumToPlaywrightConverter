document.addEventListener('DOMContentLoaded', () => {
    const statusBadge = document.getElementById('status-badge');
    const btnConvert = document.getElementById('btn-convert');
    const btnClear = document.getElementById('btn-clear');
    const btnCopy = document.getElementById('btn-copy');
    const sourceCode = document.getElementById('source-code');
    const targetCode = document.getElementById('target-code');
    const loader = document.getElementById('loader');

    // 1. Check Health of Backend/Ollama on Load
    checkHealth();

    async function checkHealth() {
        try {
            const response = await fetch('http://localhost:5000/api/health');
            const data = await response.json();

            if (data.status === 'online') {
                statusBadge.textContent = '● System Online';
                statusBadge.className = 'badge online';
                btnConvert.disabled = false;
            } else {
                statusBadge.textContent = '● Offline';
                statusBadge.className = 'badge offline';
                btnConvert.disabled = true;
            }
        } catch (e) {
            statusBadge.textContent = '● Backend Error';
            statusBadge.className = 'badge offline';
            console.error(e);
        }
    }

    // 2. Conversion Logic
    btnConvert.addEventListener('click', async () => {
        const code = sourceCode.value.trim();
        if (!code) return;

        // UI State: Loading
        btnConvert.disabled = true;
        targetCode.textContent = ''; // Clear previous
        loader.classList.remove('hidden');

        try {
            const response = await fetch('http://localhost:5000/api/convert', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code: code })
            });

            const data = await response.json();

            if (data.status === 'success') {
                targetCode.textContent = data.result;
                btnCopy.disabled = false;
            } else {
                targetCode.textContent = '// Error: ' + (data.error || 'Unknown error');
            }
        } catch (e) {
            targetCode.textContent = '// Network Error: ' + e.message;
        } finally {
            // UI State: Reset
            loader.classList.add('hidden');
            btnConvert.disabled = false;
        }
    });

    // 3. Helper Functions
    btnClear.addEventListener('click', () => {
        sourceCode.value = '';
        sourceCode.focus();
    });

    btnCopy.addEventListener('click', () => {
        if (!targetCode.textContent) return;
        navigator.clipboard.writeText(targetCode.textContent).then(() => {
            const originalText = btnCopy.textContent;
            btnCopy.textContent = 'Copied!';
            setTimeout(() => btnCopy.textContent = originalText, 2000);
        });
    });
});
