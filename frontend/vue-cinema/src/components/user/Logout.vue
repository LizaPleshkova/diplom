<template>
  <div class="log">
  </div>
</template>

<script>
  export default {
    created () {
      this.$store.dispatch('userLogout')
        .then(() => {
            console.log('from logout')
          this.$router.push('/login')
        })
    }
  }
</script>

<style>
</style>