const nodemailer = require('nodemailer');

module.exports = async (req, res) => {
    // Enable CORS for development
    res.setHeader('Access-Control-Allow-Credentials', true);
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
    res.setHeader(
        'Access-Control-Allow-Headers',
        'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
    );

    if (req.method === 'OPTIONS') {
        res.status(200).end();
        return;
    }

    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    try {
        const { name, email, phone, service, message } = req.body;

        const smtpUser = process.env.SMTP_USER || 'ceo@firstpartners.pl';
        const smtpPass = process.env.SMTP_PASSWORD;

        if (!smtpPass) {
            console.error('Missing SMTP_PASSWORD environment variable.');
            return res.status(500).json({ error: 'Konfiguracja serwera pocztowego jest niekompletna (brak hasła SMTP).' });
        }

        // Configure OVH SMTP
        const transporter = nodemailer.createTransport({
            host: 'ssl0.ovh.net',
            port: 465,
            secure: true, // true for 465, false for 587
            auth: {
                user: smtpUser,
                pass: smtpPass
            },
            tls: {
                // Do not fail on invalid certificates
                rejectUnauthorized: false
            }
        });

        const mailSubject = `Nowe zgłoszenie: ${service || 'Ogólne'} | ${name || 'Klient'}`;

        const mailOptions = {
            from: `"First Partners Kontakt" <${smtpUser}>`,
            to: 'ceo@firstpartners.pl',
            replyTo: email || smtpUser,
            subject: mailSubject,
            text: `
Nowe zgłoszenie z formularza kontaktowego:

Imię i nazwisko: ${name || 'Nie podano'}
Adres e-mail: ${email || 'Nie podano'}
Numer telefonu: ${phone || 'Nie podano'}
Wybrana usługa/temat: ${service || 'Nie podano'}

Wiadomość:
${message || 'Brak treści wiadomości'}
            `,
            html: `
<div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; border: 1px solid #c8c7bf; padding: 20px; background-color: #f9f9f7;">
    <h2 style="color: #1C3A2A; border-bottom: 1px solid #B8922A; padding-bottom: 10px;">Nowe zgłoszenie z formularza</h2>
    <p><strong>Imię i nazwisko:</strong> ${name || 'Nie podano'}</p>
    <p><strong>Adres e-mail:</strong> <a href="mailto:${email}" style="color: #B8922A;">${email || 'Nie podano'}</a></p>
    <p><strong>Numer telefonu:</strong> ${phone || 'Nie podano'}</p>
    <p><strong>Wybrana usługa/temat:</strong> ${service || 'Nie podano'}</p>
    <hr style="border: none; height: 1px; background-color: #c8c7bf; margin: 20px 0;">
    <p><strong>Wiadomość:</strong></p>
    <div style="background-color: #eeeeec; padding: 15px; border-left: 3px solid #B8922A; white-space: pre-wrap;">${message || 'Brak treści wiadomości'}</div>
</div>
            `
        };

        const info = await transporter.sendMail(mailOptions);
        console.log('Email sent successfully:', info.messageId);

        return res.status(200).json({ success: true, message: 'Email sent successfully' });
    } catch (error) {
        console.error('Error sending email:', error);
        return res.status(500).json({ error: 'Błąd podczas wysyłania wiadomości przez serwer pocztowy: ' + error.message });
    }
};
