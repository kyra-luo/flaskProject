function toggleSection(className, headerRow) {
    const sections = document.querySelectorAll('.' + className);
    const arrow = headerRow.querySelector('.arrow');

    sections.forEach(section => {
        if (section.style.display === 'block') {
            section.style.display = 'none';
            arrow.innerHTML = '&#9660;';  // 确保这里没有额外的添加操作
        } else {
            section.style.display = 'block';
            arrow.innerHTML = '&#9650;';  // 确保这里没有额外的添加操作
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
            const response = await fetch('https://example.com/api/user-stats');  // 替换为你的API URL
            const data = await response.json();
            document.getElementById('postKarma').textContent = data.postKarma;
            document.getElementById('commentKarma').textContent = data.commentKarma;
            document.getElementById('goldReceived').textContent = data.goldReceived;
        } catch (error) {
            console.error('Error fetching data: ', error);
        }
    }

    setInterval(fetchData, 30000);  // 定时刷新数据，每30秒更新一次
    fetchData();  // 初始加载数据
});

function addSocialLink() {
    alert("Add social link functionality to be implemented.");
}
