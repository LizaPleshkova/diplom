import { createRouter, createWebHistory } from "vue-router";
// import { CinemaList } from "../components/CinemaList"
// import {MovieList} from '../components/MovieList'
// import CinemaDataService from "./services/DataService";

const routes = [
  {
    path: "/",
    name: "main",
    component: () => import("../components/base/Main.vue"),
  },
  {
    path: "/movie",
    name: "movie-list",
    // component: CinemaDataService,
    component: () => import("../components/MovieList.vue"),
  },
  {
    path: "/movie/:movieId",
    name: "movie-detail",
    // component: CinemaDataService,
    component: () => import("../components/Movie.vue"),
    props: true,
  },
  {
    path: "/cinema",
    name: "cinema-list",
    //   component: CinemaList,
    component: () => import("../components/CinemaList.vue"),
  },
  {
    path: "/cinema/:cinemaId",
    name: "cinema-detail",
    component: () => import("../components/CinemaDetail.vue"),
    props: true,
  },
  {
    path: "/login",
    component: () => import("../components/user/Login.vue"),
  },
  {
    path: "/register",
    component: () => import("../components/user/Register.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
router.beforeEach((to, from, next) => {
  const publicPages = ['/login', '/register', '/home'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user');
  // trying to access a restricted page + not logged in
  // redirect to login page
  if (authRequired && !loggedIn) {
    next('/login');
  } else {
    next();
  }
});

export default router;
