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


// document.getElementById('shareButton').addEventListener('click', () => {
//     const shareOptions = document.getElementById('shareOptions');
//     shareOptions.classList.toggle('d-none');
// });



function addSocialLink() {
    alert("Add social link functionality to be implemented.");
}



function editAboutMe() {
    console.log("Function called"); // 检查是否被调用
    console.log("test test")
    document.getElementById('editModal').style.display = 'block'; // 显示编辑框
}

function saveAboutMe() {
    const newContent = document.getElementById('newAboutMe').value; // 获取新输入的内容
    document.getElementById('editModal').style.display = 'none'; // 隐藏编辑框

    fetch('/user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('input[name="csrf_token"]').value // 确保传递 CSRF 令牌
        },
        body: JSON.stringify({ aboutMe: newContent })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('aboutMeText').innerText = newContent; // 更新页面显示
            alert('Profile updated successfully!');
        } else {
            throw new Error(data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error updating profile: ' + error);
    });
}
 function test_click() {
     document.getElementsByClassName('useredit')
     console.log("hello")
 }

