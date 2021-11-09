let users;

const start = () => {
  console.log(users);
  const form = document.querySelector('form'),
    loginInput = document.getElementById('login'),
    passwordInput = document.getElementById('password');

  form.addEventListener('submit', event => {
    document.querySelector('.error-password').style.display = "none";
    document.querySelector('.error-email').style.display = "none";
    event.preventDefault();
    const userEmail = loginInput.value;
    const userPassword = passwordInput.value;

    let flag = true;
    users.forEach(user => {
      if (userEmail === user.login) {
        flag = false;
        if (userPassword === user.password) {
          window.location.href = './timetable.html';
        } else {
          document.querySelector('.error-password').style.display = "block";
        }
      }
    });
    if (flag) document.querySelector('.error-email').style.display = "block";


  });
};

const getAllInfo = () => {
  fetch("./db/users.json")
    .then(response => {
      if (response.status !== 200) throw new Error("Status network not 200");
      return response.json();
    })
    .then(data => {
      users = data;
      start();
    })
    .catch(error => console.error(error));
};
getAllInfo();

