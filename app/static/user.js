function toggleSection(className, headerRow) {
    const sections = document.querySelectorAll('.' + className);
    const arrow = headerRow.querySelector('.arrow');

    sections.forEach(section => {
        if (section.style.display === 'block') {
            section.style.display = 'none';
            arrow.innerHTML = '&#9660;';
        } else {
            section.style.display = 'block';
            arrow.innerHTML = '&#9650;';
        }
    });
}


document.getElementById('shareButton').addEventListener('click', () => {
    const shareOptions = document.getElementById('shareOptions');
    shareOptions.classList.toggle('d-none');
});

document.addEventListener('DOMContentLoaded', async () => {
    async function fetchData() {
        try {
            const response = await fetch('https://example.com/api/user-stats');
            const data = await response.json();
            document.getElementById('postKarma').textContent = data.postKarma;
            document.getElementById('commentKarma').textContent = data.commentKarma;
            document.getElementById('goldReceived').textContent = data.goldReceived;
        } catch (error) {
            console.error('Error fetching data: ', error);
        }
    }

    //refresh every 30s
    setInterval(fetchData, 30000);
    //init loading data
    fetchData();
});

function addSocialLink() {
    alert("Add social link functionality to be implemented.");
}
