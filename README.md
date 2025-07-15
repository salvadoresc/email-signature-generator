
# HTML Email Signature Generator

This project generates professional HTML email signatures using a CSV file as input and a flexible template system.

🛠 Built with:
- Python
- Jinja2 for templating
- Pandas for CSV handling

## Features
- Generate personalized email signatures from a simple spreadsheet
- Shared branding (logo, contact info, social links) controlled via `settings.json`
- Automatically uses default values for missing fields
- Outputs each signature as a standalone `.html` file in the `output_signatures` folder

## Usage

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install pandas jinja2
   ```
3. Edit `staff.csv` with your team’s information.
4. Adjust branding or social media in `settings.json`.
5. Run the generator:
   ```bash
   python generate_signatures.py
   ```

## Example Input

**staff.csv**
```csv
name,title,pronouns,email,phone,img_url,specialties
Camila López,Creative Director,She/Her,camila@haycoctelesamor.com,,https://static.vecteezy.com/system/resources/previews/036/594/092/large_2x/man-empty-avatar-photo-placeholder-for-social-networks-resumes-forums-and-dating-sites-male-and-female-no-photo-images-for-unfilled-user-profile-free-vector.jpg,Cocktail Design|Brand Partnerships|Event Strategy
Luis Méndez,Operations Manager,He/Him,luis@haycoctelesamor.com,,https://static.vecteezy.com/system/resources/previews/036/594/092/large_2x/man-empty-avatar-photo-placeholder-for-social-networks-resumes-forums-and-dating-sites-male-and-female-no-photo-images-for-unfilled-user-profile-free-vector.jpg,Event Logistics|Supplier Coordination|Staff Management
Pedro Picapiedras, Bronto crane operator,He/Him,pedro@haycoctelesamor.com,,https://static.vecteezy.com/system/resources/previews/036/594/092/large_2x/man-empty-avatar-photo-placeholder-for-social-networks-resumes-forums-and-dating-sites-male-and-female-no-photo-images-for-unfilled-user-profile-free-vector.jpg,Event Logistics|Supplier Coordination|Staff Management

```

## Author

**Emigdio Salvador Corado**

## License

MIT License
