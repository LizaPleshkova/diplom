import { createRouter, createWebHistory } from "vue-router";
// import { CinemaList } from "../components/CinemaList"
// import {MovieList} from '../components/MovieList'
// import CinemaDataService from "./services/DataService";
// import Vue from "vue";
// import VueRouter from "vue-router";

// Vue.use(VueRouter);

const ifNotAuthenticated = (to, from, next) => {
  // console.log("here", store.authModule.user.getters.isAuthenticated);
  const loggedIn = localStorage.getItem("token");
  if (!loggedIn) {
    next();
    console.log("here2");
    return;
  }
  next("/");
};

const ifAuthenticated = (to, from, next) => {
  const loggedIn = localStorage.getItem("token");
  if (loggedIn) {
    next();
    return;
  }
  next("/login");
};


const routes= [
    {
      path: "/",
      name: "main",
      component: () => import("../components/base/Main.vue"),
    },
    {
      path: "/movie/",
      name: "movie-list",
      // component: CinemaDataService,
      component: () => import("../components/MovieList.vue"),
    },
    {
      path: "/movie/:movieId/",
      name: "movie-detail",
      // component: CinemaDataService,
      component: () => import("../components/MovieDetail.vue"),
      props: true,
      // beforeEnter: ifNotAuthenticated,
    },
    {
      path: "/movie-session/:movieSessionId/",
      name: "movie-session",
      component: () => import("../components/MovieSessionSeats.vue"),
      props: true,
    },
    {
      path: "/cinema/",
      name: "cinema-list",
      //   component: CinemaList,
      component: () => import("../components/CinemaList.vue"),
      
    },
    {
      path: "/cinema/:cinemaId/",
      name: "cinema-detail",
      component: () => import("../components/CinemaDetail.vue"),
      props: true,
    },

    {
      path: "/login/",
      name: "login",
      component: () => import("../components/user/Login.vue"),
    },
    {
      path: "/signup/",
      component: () => import("../components/user/Signup.vue"),
    },
    {
      path: "/logout/",
      component: () => import("../components/user/Logout.vue"),
      
    },
    {
      path: "/profile/",
      component: () => import("../components/user/Profile.vue"),
      props: true,
      beforeEnter: ifAuthenticated,

    },
    {
      path: "/profile/tickets/",
      name: "user-tickets",
      component: () => import("../components/user/Tickets.vue"),
      props: true,
    },
  ]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
// router.beforeEach((to, from, next) => {
//   console.log(to.path);
//   const publicPages = ['/login/', '/signup/', '/', '/cinema/', '/movie/'];
//   const authRequired = !publicPages.includes(to.path);
//   console.log(authRequired)
//   const loggedIn = localStorage.getItem('token');
//   // trying to access a restricted page + not logged in
//   // redirect to login page
//   if (authRequired && !loggedIn) {
//     next('/login');
//   } else {
//     next();
//   }
// });

export default router;
