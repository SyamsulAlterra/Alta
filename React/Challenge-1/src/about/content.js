import React from 'react'
import '../css/about.css'
import '../css/bootstrap.min.css'
import altav2x from "../img/logo-ALTA@2x.png"
import imgdot from "../img/img-dot.png"
import matthew from "../img/matthew-hamilton-tNCH0sKSZbA-unsplash.jpg" 
import fb from "../img/ic_fb.png"
import twitter from "../img/ic-twitter.png"
import instagram from "../img/ic-instagram.png"
import linkedin from "../img/ic-linkedin.png"
import logoAltaV2 from "../img/logo-ALTA-v2.png"

export class Content extends React.Component{
    render(){
        return (
<div>
<div>
    <header>
        <div class="container toppage">
            <div class="row align-items-center">
                    <div class="col-md-4">
                        <div class="header-logo">
                            <a class="logo-navigasi pull-left" href="home.html">
                                <img src={altav2x} alt="image" />
                            </a>
                        </div>
                    </div>
                    <div class="col-md-8 topnav" id="myTopnav">
                        <div class="text-right wordtopright">
                                <ul>
                                    <a href="home.html">
                                        <li>
                                            HOME
                                        </li>
                                    </a>
                                    <a href="about.html">
                                        <li class="pageSekarang">
                                            ABOUT
                                        </li>
                                    </a>
                                    <a href="page-experience.html">
                                        <li>
                                            EXPERIENCE
                                        </li>
                                    </a>
                                    <a href="contact.html">
                                        <li>
                                            CONTACT
                                        </li>
                                    </a>
                                    <a href="javascript:void(0);" class="icon" onclick="myFunction()"><i class="fa fa-bars"></i>
                                    </a>
                                </ul>
                        </div>
                    </div>
            </div>
            </div>
    </header>
    <div class="container-fluid">
        <div class="row aboutme align-items-center">
                <div class="container">
                    <div class="background2">
                        <h2>ABOUT ME.</h2>
                    </div>
                </div>
        </div>
    </div>
    <div class="container">
        <div class="row SettingRow3">
            <div class="col-md-7">
                <div class="content-paragraph">
                    <p>
                        Hello! I’m Anne Sullivan, a full-stack engineer based in Malang, IDN who enjoys building things that live on the internet. I develop exceptional websites and web apps that provide intuitive, pixel-perfect user interfaces with efficient and modern backends. 
                    </p>
                    <p>
                        Shortly after graduating from Alterra Academy, I joined the engineering team at Alterra where I work on a wide variety of interesting and meaningful projects on a daily basis.
                    </p>                       
                    <p>Here’s few technologies 
                        I’ve been working with recently :
                    </p>
                    </div>
                    <table class="table table-bordered">
                        <tbody>
                            <tr>
                                <td>HTML & CSS</td>
                                <td>Serverless</td>
                                <td>Scrum</td>
                            </tr>
                            <tr>
                                <td>Programming</td>
                                <td>Restful API</td>
                                <td>Test-Driven Dev</td>
                            </tr>
                            <tr>
    
                                <td>Database</td>
                                <td>Javascript</td>
                                <td>Software Testing</td>
                            </tr>
                            <tr>
       
                                <td>Git & Github</td>
                                <td>Single Page App</td>
                                <td>UI/UX Designer</td>
                            </tr>
                            
                        </tbody>
                    </table>
                </div>
                <div class="col-md-5">
                    <div class="imagePicture">
                                
                                <img src={imgdot} class="img-fluid image1" alt="Responsive image" />
                                <img src={matthew} class="img-fluid image2" alt="Responsive image" />
                            </div>
                    </div>
                </div>
            </div>
        </div>
    <footer>
        <div class="container-fluid alterrabawah">
            <div class="row align-items-center">
                <div class="col-md-5">
                    <div class="AlterraBawah">
                        
                        <img src={logoAltaV2} alt="..." class="Responsive image" />
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="vl">
                        <div class="socialmedia">
                            <p>Social Media</p>
                            
                            <img src={fb} alt="..." class="Responsive image"/><img src={twitter} alt="..." class="Responsive image"/><img src={instagram} alt="..." class="Responsive image"/><img src={linkedin} alt="..." class="Responsive image"/>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="verticaLine">
                        <div class="copyright">
                            Copyright @ 2019 Alterra
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>
</div>
        )
    }
}