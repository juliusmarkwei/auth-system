import React from 'react'
import Navbar from '../components/Navbar'


function Layout(props) {
  return (
    <div>
        <Navbar />
        {props.children}
    </div>
  )
}

export default Layout