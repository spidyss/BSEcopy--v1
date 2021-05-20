<template>
  <nav class="navbar navbar-light">
    <div class="container">
      <router-link to="/">
        <small class="logo"><span class="text-bold">Bhav</span>Copy</small>
      </router-link>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  text-decoration: none;
  color: black;
}
</style>
