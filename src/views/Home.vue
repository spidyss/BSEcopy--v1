<template>
  <div>
    <NavBar></NavBar>
    <div class="container">
      <div class="mt-5 pt-5"  >
        <div class="row mb-4 mt-5 pt-5 text-center">
          <div class="col-sm">
            <h1 class="logo font-56"><span class="text-bold">Bhav</span>Copy</h1>
            <small class="text-grey">Search scrip name in the latest BSE Equity BhavCopy.</small>
          </div>
        </div>
        <div class="row px-4">
          <SearchBar></SearchBar>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '../components/NavBar';
import SearchBar from '../components/SearchBar';

export default {
  name: 'Home',
  components: {
    NavBar,
    SearchBar
  }
}
</script>

<style scoped>
</style>
