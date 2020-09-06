<template>
  <div>
    <div>
      <img src="@/assets/logo2.png" class="logo2">
  </div>
  <div>
      <img src="@/assets/title.png" class="title">
  </div>

  </div>

</template>

<script>
import { mapGetters } from 'vuex'
import Logo from './Logo'
import SidebarItem from './SidebarItem'
import variables from '@/styles/variables.scss'

export default {
  components: { SidebarItem, Logo },
  computed: {
    ...mapGetters([
      'sidebar'
    ]),
    routes() {
      return this.$router.options.routes
    },
    activeMenu() {
      const route = this.$route
      const { meta, path } = route
      // if set path, the sidebar will highlight the path you set
      // if (meta.activeMenu) {
      //   return meta.activeMenu
      // }
      return path
    },
    showLogo() {
      return this.$store.state.settings.sidebarLogo
    },
    variables() {
      return variables
    },
    isCollapse() {
      return !this.sidebar.opened
    }
  }
}
</script>
<style scoped>
.logo2{
  position: absolute;
  top: 20%;
  left: 12%;
  height: 18%;
 }
.title{
  position: absolute;
  top: 23%;
  left: -25%;
  height: 62%;
}
</style>
