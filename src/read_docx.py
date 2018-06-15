import pandas as pd
import docx2txt
import re


def read_questions(filename, trivia_year):
    '''Takes in filename and puts questions into pandas dataframe. The shutout, action, and thrownout notes are in the answer for the question before it. '''
    my_text = docx2txt.process(filename)
    l_questions = my_text.split('#')
    l_questions = l_questions[1:]

    years = []
    q_numbers = []
    questions = []
    q_answers = []

    # counter = 0

    for questioni in l_questions:
        # counter += 1
        # print(counter)
        year = trivia_year
        q_number, question_answer = questioni.split('Q:')
        q_a_check = question_answer.split('A:')
        if len(q_a_check) > 1:
            question = q_a_check[0]
            answer = q_a_check[1]
        else:
            question = q_a_check[0]
            answer = None
        final_num = re.sub(r"[\n\t]*", "", q_number)
        stepq = re.sub(r"[\n\t]*", "", str(question))
        final_q = re.sub('\s+', ' ', stepq).strip()
        stepa = re.sub(r"[\n\t]*", "", str(answer))
        final_a = re.sub('\s+', ' ', stepa).strip()
        years.append(year)
        q_numbers.append(final_num)
        questions.append(final_q)
        q_answers.append(final_a)

    df = pd.DataFrame({'q_answer':q_answers,'question':questions, 'q_number':q_numbers,'year':years, 'source': ''})

    return df


if __name__ == '__main__':
    df1994 = read_questions('data/Trivia_Questions_1994.docx', 1994)
    df1995 = read_questions('data/Trivia_Questions_1995.docx', 1995)
    df1996 = read_questions('data/Trivia_Questions_1996.docx', 1996)
    df1997 = read_questions('data/Trivia_Questions_1997.docx', 1997)
    df1998 = read_questions('data/Trivia_Questions_1998.docx', 1998)
    df1999 = read_questions('data/Trivia_Questions_1999.docx', 1999)
    df2000 = read_questions('data/Trivia_Questions_2000.docx', 2000)
    df2001 = read_questions('data/Trivia_Questions_2001.docx', 2001)
    df2003 = read_questions('data/Trivia_Questions_2003.docx', 2003)
    df2004 = read_questions('data/Trivia_Questions_2004.docx', 2004)
    df2006 = read_questions("data/Trivia_Questions_2006.docx", 2006)
    df2007 = read_questions('data/Trivia_Questions_2007.docx', 2007)
    df2010 = read_questions('data/Trivia_Questions_2010.docx', 2010)
    df2011 = read_questions('data/Trivia_Questions_2011.docx', 2011)
    df2012 = pd.read_csv('data/Trivia_questions_2012.csv', encoding='latin-1')
    frames = [df1994, df1995, df1996, df1997, df1998, df1999, df2000, df2001, df2003, df2004, df2006, df2007, df2010, df2011, df2012]

    q_df = pd.concat(frames)
    q_df.to_csv('data/merged_question.csv')
