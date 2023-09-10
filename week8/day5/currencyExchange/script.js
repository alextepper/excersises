const fromCurrency = document.getElementById('fromCurrency');
const toCurrency = document.getElementById('toCurrency');
const amount = document.getElementById('amount');
const convertedAmount = document.getElementById('convertedAmount');
const switchBtn = document.getElementById('switch');
const convertBtn = document.getElementById('convert');


document.addEventListener('DOMContentLoaded', () => {
    fetch('https://v6.exchangerate-api.com/v6/d2480b6f2b44a596957abf4e/codes')
        .then(response => response.json())
        .then(data => {
            const supportedCodes = data.supported_codes;
            supportedCodes.forEach(currency => {
                const code = currency[0];
                const name = currency[1];

                const optionFrom = document.createElement('option');
                optionFrom.value = code;
                optionFrom.textContent = `${code} - ${name}`;
                fromCurrency.appendChild(optionFrom);

                const optionTo = optionFrom.cloneNode(true);
                toCurrency.appendChild(optionTo);
            });
        })
        .catch(error => console.error('Error fetching currency codes:', error));
});


convertBtn.addEventListener('click', () => {
    const from = fromCurrency.value;
    const to = toCurrency.value;
    const amt = amount.value;

    fetch(`https://v6.exchangerate-api.com/v6/d2480b6f2b44a596957abf4e/pair/${from}/${to}/${amt}`)
        .then(response => response.json())
        .then(data => {
            convertedAmount.value = data.conversion_result.toFixed(2);
        })
        .catch(error => console.error('Error converting currencies:', error));
});


switchBtn.addEventListener('click', () => {
    const temp = fromCurrency.value;
    fromCurrency.value = toCurrency.value;
    toCurrency.value = temp;
    convertedAmount.value = '';
});
