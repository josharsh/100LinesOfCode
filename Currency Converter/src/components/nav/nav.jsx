
import React from 'react'
import "./nav.css"

export default function nav() {
  return (
    <div>
      <div className='sidebar'>
        <ul>
            <li>
                <h1>Abhinab Choudury</h1>
            </li>
            <li>
            <a className='aline-link' href="https://www.instagram.com/_abhinab_choudhury_/" target="_blank" rel="noopener noreferrer"> 
                <img width="23" height="23" src="https://img.icons8.com/fluency/48/instagram-new.png" alt="instagram-new"/>
                Instgram
            </a>
            </li>
            <li>
            <a className='aline-link' href="https://www.linkedin.com/in/abhinab-choudhury-18022822b" target="_blank" rel="noopener noreferrer"> 
                <img width="23" height="23" src="https://img.icons8.com/color/48/linkedin.png" alt="linkedin"/>
                Linkedin
            </a>
            </li>
            <li>
            <a className='aline-link' href="https://twitter.com/abhinabc_" target="_blank" rel="noopener noreferrer"> 
            <img width="23" height="23" src="https://img.icons8.com/ios/50/twitterx--v1.png" alt="twitterx--v1"/>
                Twitter
            </a>
            </li>
        </ul>
      </div>
    </div>
  )
}
