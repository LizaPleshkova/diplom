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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
