<template>
  <div class="center-screen mx-auto">
    <div class="row h-100 justify-content-center px-4">
        <div class="col-sm my-auto text-center">
            <div class="card">
                <div class="card-body">
                    <p class="card-text font-24">Sorry we couldn't find<br>any matches for "<span class="text-bold">{{ name }}</span>"</p>
                    <router-link to="/"><button class="btn btn-success border-0">TRY AGAIN</button></router-link>
                </div>
            </div>
        </div>
    </div>        
  </div>
</template>

<script>
export default {
  name: 'NoMatch',
  props: {
    name: {
      type: String
    }
  }
}
</script>

<style scoped>
.center-screen {
  max-width: 600px;
  display: block;
  height: 100vh;
}

.card {
  border: 0px;
  border-radius: 10px;
}

.font-24 {
    font-size: 24px;
}

.btn-success {
  border-radius: 20px;
  padding-left: 30px;
  padding-right: 30px;
}
</style>
