<template>
  <div class="dashboard-container">
    <div class="dashboard-text">name: {{ name }}</div>
    <h1> {{ name }} </h1>
  </div>
</template>

<script>
// import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  data() {
    return {
      name: ''
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      this.axios
        .post('/hello_api', {
          input: 'nihao'
        })
        .then((res) => {
          this.name = res.data['hello']
        })
        .catch((error) => {
          alert(error)
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
