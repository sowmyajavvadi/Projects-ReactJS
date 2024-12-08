import React, { useState } from "react";
// import '/Users/sowmyajavvadi/Projects/frontend/src/App.css';
import './SideMenuBar.css';
import { FaBars, FaBusAlt } from "react-icons/fa";
import { MdBusAlert, MdBusinessCenter } from "react-icons/md";
import { TbUsersGroup, TbBusinessplan } from "react-icons/tb";

import { TiBusinessCard } from "react-icons/ti";
import { FaScrewdriverWrench } from "react-icons/fa6";
import { NavLink } from "react-router-dom";
import { IoIosContact } from "react-icons/io";

const SideMenuBar=({children})=>{
    const [isOpen ,setIsOpen]= useState(false);
    const toggle=()=>setIsOpen(!isOpen);
    const menuItem=[
        {
            path:"/",
            name:"Login ",
            icon:<IoIosContact />
        },
        {
            path:"/VehicleDetails",
            name:"VehicleDetails ",
            icon:<FaBusAlt />
        },
        {
            path:"/VehicleInstallments",
            name:"VehicleInstallments ",
            icon:<MdBusinessCenter />
        },
        {
            path:"/GarageExpenses",
            name:"GarageExpenses ",
            icon:<FaScrewdriverWrench />
        },
        {
            path:"/EmployeeDetails",
            name:"EmployeeDetails ",
            icon:<TiBusinessCard />
        },
        {
            path:"/TrafficFines",
            name:"TrafficFines ",
            icon:<MdBusAlert />
        },
        {
            path:"/SupplierDetails",
            name:"SupplierDetails ",
            icon:<TbUsersGroup />
        },
        {
            path:"/ClientPaymentDetails",
            name:"ClientPaymentDetails ",
            icon:<TbBusinessplan />
        },

    ]
    return (
        <div className="container">
            <div style={{width:isOpen ? "300px" : "50px" }} className="sidebar">
                <div className="top_section">
                    <h1 style={{display:isOpen ? "block" :"none" }}className="Menu">Menu</h1>
                    <div style={{marginLeft:isOpen ? "50px" :"0px" }}className="bars">
                        <FaBars onClick={toggle}/>
                    </div>
                </div>
                    {
                        menuItem.map((item,index)=>(
                            <NavLink to={item.path} key={index} className="link" activeclassName="active">
                                <div className="icon">{item.icon}</div>
                                <div style={{display:isOpen ? "block": "none"}}className="link_text">{item.name}</div>

                            </NavLink>
                        ))
                    }
            </div>
            <main>{children}</main>
        </div>

    )

}


export default SideMenuBar;