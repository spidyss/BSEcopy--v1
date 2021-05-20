<template>
  <div class="center-screen mx-auto">
    <div class="row h-100 justify-content-center">
      <div class="spinner-border my-auto" role="status">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Spinner'
}
</script>

<style scoped>
.center-screen {
  max-width: 600px;
  display: block;
  height: 100vh;
}

.spinner-border {
  width: 5rem;
  height: 5rem;
}
</style>
