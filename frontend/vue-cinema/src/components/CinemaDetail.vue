<template>
    <div class="card" >
        <h1>cinema</h1>
    </div>
                    
</template>

<script>
export default {
  name: 'cinema-detail',
  props:{
      cinema:{
          type:Object,
          default:()=>{}
      }
  },
//   created() {
//     const cinema = cinemas.find(cinema => cinema.id == this.$route.params.id)
//     if (cinema) {
//       this.cinema = cinema
//     }
//   }


}
</script>