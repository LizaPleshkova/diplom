import {HTTP_USER} from '@/http-common.js'

class AuthService {
  login(user) {
    return HTTP_USER
      .post('/token-auth/', {
        username: user.username,
        password: user.password
      })
      .then(response => {
        if (response.data.accessToken) {
          localStorage.setItem('user', JSON.stringify(response.data));
        }
        return response.data;
      });
  }
  logout() {
    localStorage.removeItem('user');
  }
  register(user) {
        console.log(user);

    return HTTP_USER.post('/register/', {
      username: user.username,
      email: user.email,
      password: user.password,
      birth_date:user.birth_date
    });
  }
}

export default new AuthService();