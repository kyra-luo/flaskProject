function toggleSection(className, headerRow) {
    var sections = document.querySelectorAll('.' + className);
    var arrow = headerRow.querySelector('.arrow');
    
    sections.forEach(function(section) {
        if (section.style.display === 'block') {
            section.style.display = 'none';  // 设置为隐藏
            arrow.innerHTML = '&#9660;'; // 箭头向下
        } else {
            section.style.display = 'block';  // 设置为显示
            arrow.innerHTML = '&#9650;'; // 箭头向上
        }
    });
}


document.getElementById('shareButton').addEventListener('click', function() {
    var shareOptions = document.getElementById('shareOptions');
    if (shareOptions.classList.contains('hidden')) {
        shareOptions.classList.remove('hidden');
    } else {
        shareOptions.classList.add('hidden');
    }
});


document.addEventListener('DOMContentLoaded', function() {
    function fetchData() {
        fetch('https://example.com/api/user-stats')  // 替换为你的API URL
            .then(response => response.json())
            .then(data => {
                document.getElementById('postKarma').textContent = data.postKarma;
                document.getElementById('commentKarma').textContent = data.commentKarma;
                document.getElementById('goldReceived').textContent = data.goldReceived;
                // 日期通常是固定的，不需要更新
            })
            .catch(error => console.error('Error fetching data: ', error));
    }

    // 定时刷新数据，每30秒更新一次
    setInterval(fetchData, 30000);

    // 初始加载数据
    fetchData();
});


function addSocialLink() {
    alert("Add social link functionality to be implemented.");
}