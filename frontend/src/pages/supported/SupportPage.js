import React from 'react';
import { Container } from 'react-bootstrap';
import appstyles from '../../App.module.css';
import TeamsDropdown from '../../components/TeamsDropdown';
import { useProfileData } from '../../contexts/ProfileDataContext';

const TeamSelector = ({ mobile }) => {

    const { teamselector } = useProfileData();


    return (
        <Container className={`${appStyles.Content} ${mobile && 'd-lg-none text-center mb-3'}`}>
            <>
                <TeamsDropdown />
            </>
        </Container>
    )
}

export default SupportPage;
