import { createRouter, createWebHistory } from 'vue-router'
// import { CinemaList } from "../components/CinemaList"
// import {MovieList} from '../components/MovieList'
// import Main from '../components/base/Main'




const routes = [
    // {
    //     path: '/',
    //     name: 'main',
    //     component: Main
    //   },
    {
      path: '/',
      name: 'movie-list',
    //   component: MovieList
      component: () => import( '../components/MovieList.vue')
    },
    {
      path: '/cinema',
      name: 'cinema-list',
    //   component: CinemaList,
    component: () => import( '../components/CinemaList.vue'),
    children: [
      {
        path: '',
        name: 'cinema-list',
        component: () => import( '../components/CinemaList.vue'),
      },
      {
        path: ':id',
        name: 'cinema',
        component: () => import( '../components/Cinema.vue'),
      },
      // {
      //   path: '/:catchAll(.*)',
      //   redirect: { name: 'cinema-list' }
      // },
    ]

   
    }
  ]
  const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  })
  export default router