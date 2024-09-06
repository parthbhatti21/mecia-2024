from cohere import Client
import audio
import Web1
api_key = "FvgXRMGeiYpsMoJfym1pffFKgquICXPs0IeHuTKi"

client = Client(api_key=api_key)
def ai(text):
    data="""
**Departments at SVIT**

1. **Computer Engineering**
   - About: Established in 1998, offering UG and PG programs. Focuses on industry exposure, skill development, and placements.
   - Vision: Develop globally competent engineers with strong technical and ethical foundations.
   - Mission: Strengthen fundamentals, foster innovation, and cultivate ethical values.

2. **Information Technology**
   - About: Established in 1998, expanded intake to 120 by 2011. Focuses on cybersecurity and practical experience.
   - Vision: Provide high-quality education and foster research.
   - Mission: Equip students with IT fundamentals, leadership skills, and ethical responsibility.

3. **Electrical Engineering**
   - About: Established in 1997, offering UG and ME programs with advanced labs and industry collaborations.
   - Vision: Develop globally competitive engineers.
   - Mission: Impart cutting-edge knowledge and encourage lifelong learning.

4. **Aeronautical Engineering**
   - About: Established in 2003, focusing on aircraft, helicopters, and missile technology through internships and workshops.
   - Vision: Become a premier center for academic excellence in aviation.
   - Mission: Develop skilled aerospace professionals and foster innovation.

5. **Civil Engineering**
   - About: Established in 1997, known for labs and research in environmental audits. Focuses on national development.
   - Vision: Be a premier center for civil engineering education.
   - Mission: Promote holistic student growth and faculty development.

6. **Computer Science & Design**
   - About: Emphasizes hands-on learning, industry collaboration, and research in graphics.
   - Vision: Develop globally competent engineers.
   - Mission: Build strong fundamentals, promote innovation, and instill ethical values.

7. **Mechanical Engineering**
   - About: Established in 1997, offering UG and PG programs with a focus on workshops and creativity.
   - Vision: Prepare engineers to meet industry needs.
   - Mission: Adopt outcome-based education and nurture creativity and sustainability.

8. **Electronics & Communication Engineering**
   - About: Established in 1999, focuses on VLSI, embedded technologies, and hands-on experience.
   - Vision: Produce globally competitive engineers with innovation.
   - Mission: Provide excellence in teaching and research.

**Fees and Structure**  
- All Programs: ₹78,500 (First Year)

---

**Bus Services**  
SVIT provides daily transport facilities from Vadodara to SVIT and back. For assistance, contact:
- Swapnil Patel, Pushpam Travels: +91 99788 88837
- Bhavinbhai Patel, Shree Ambika Travels: +91 94263 80208
- Chintan Patel, Shree Ambika Travels: +91 97237 27040
- Sunny Patel, Jay Ambe Travels: +91 72268 99534

---

**Hostel**  
SVIT offers residential facilities through separate hostels for boys and girls within a 3 km radius. Hostels provide clean, secure rooms with Wi-Fi and meal services. The girls' hostel includes a cooking space and food service options, while the boys' hostel provides tiffin services with various food choices.

---

**Sports**  
SVIT promotes fitness and teamwork through various sports such as cricket, football, badminton, volleyball, and kabaddi. Participation in sports helps develop physical fitness, mental strength, confidence, and decision-making skills.

---

**Training & Placement (T&P) Cell**  
- Objective: Prepares students for recruitment through training on group discussions, interviews, and personality development.
- Activities: Mock tests, technical training, workshops, seminars, and placement drives.
- Placement Officer: Prof. Tejas Ghotikar (placement@svitvasad.ac.in | +91 93167 70768)

---

**Events**  
1. **Prakarsh - Techfest and Talkfest**  
   - A national symposium with 50 technical and non-technical events, including robotics and workshops, attracting 3,500 students annually from 80 colleges.
  
2. **Malhar - Cultural and Sports Events**  
   - Organized by the Students' Central Committee, focusing on student welfare through cultural and sporting events, teamwork, and fitness.

3. **Spandan**  
   - A one-day festival for new students to showcase their talents, preparing them for the Annual Day in the even semester.

---

**Vision and Mission**  
- Vision: Prepare students for future challenges by fostering teamwork, professional ethics, and fitness.
- Mission: Celebrate cultural events, organize sports week, appoint students to leadership roles, and provide financial aid to economically disadvantaged students.

---

**Research & Development (R&D)**  
- Objective: Foster a research-oriented environment for students and faculty.
- Initiatives: Faculty awareness programs, support for R&D proposals, and professional growth through workshops.
- Milestones: MOU with GERMI for renewable energy research, GUJCOST-DST sanctioned projects, and increased sponsored research funding by 10%.
- R&D Cell: Oversees research programs, encouraging collaborations with industries and supporting grant applications.

Above is a call scipt use this knowledge to answer the below question.
"""
    prompt = data+text+"generate small response!"
    model = "command"

    try:
        response = client.generate(model=model, prompt=prompt)

        generations = response.generations
        for generation in generations:
            # print("Assistant: ",generation.text)
            if(Web1.stop_flag):
               return
            else:
               audio.text_to_audio_and_play(generation.text)
        
    except Exception as e:
        print("An error occurred:", str(e))