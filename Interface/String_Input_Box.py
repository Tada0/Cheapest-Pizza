import pygame
from Graphics.Color_Handler import Color


class StringInputBox:
    available_keys = [
        pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
        pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
        pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e,
        pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j,
        pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o,
        pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t,
        pygame.K_u, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z,
        pygame.K_DELETE, pygame.K_LEFT, pygame.K_RIGHT,
        pygame.K_SPACE, pygame.K_SLASH, pygame.K_BACKSPACE,
        pygame.K_ESCAPE, pygame.K_RETURN]

    unsupported_characters = [
        'ą', 'ę', 'ć', 'ł', 'ó', 'ż', 'ź', 'ś', 'ń'
    ]

    def __init__(self, x, y, max_length, width, start_value):

        self.x = x
        self.y = y
        self.font = 'Graphics/y.n.w.u.a.y.ttf'
        self.caret_position = len(str(start_value))
        self.tick_time = 20
        self.caret_timer = self.tick_time
        self.caret_visible = True
        self.rect = pygame.Rect(x, y, width, 32)
        self.color = Color('BLACK')
        self.text = str(start_value)
        self.txt_surface = pygame.font.Font(None, 16).render(self.text, True, self.color)
        self.active = False
        self.max_length = max_length

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the input_box rect
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box
            self.color = Color('WHITE') if self.active else Color('BLACK')

        if event.type == pygame.KEYDOWN:

            if self.active:

                if event.key not in StringInputBox.available_keys:
                    pass

                elif event.key == pygame.K_BACKSPACE:

                    self.text = self.text[:self.caret_position - 1] + self.text[self.caret_position:]

                    if len(self.text) > 0:
                        self.caret_position -= 1

                elif event.key == pygame.K_DELETE:

                    if self.caret_position < len(self.text):
                        self.text = self.text[:self.caret_position] + self.text[self.caret_position + 1:]

                elif event.key == pygame.K_LEFT:
                    self.caret_position -= 1

                elif event.key == pygame.K_RIGHT:

                    if self.caret_position < len(self.text):
                        self.caret_position += 1

                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:

                    self.active = False
                    self.color = Color('BLACK')

                else:

                    if len(self.text) < self.max_length:
                        if event.unicode not in StringInputBox.unsupported_characters:
                            self.text = self.text[:self.caret_position] + event.unicode + self.text[
                                                                                          self.caret_position:]
                            self.caret_position += 1

                # Re-render the text
                self.txt_surface = pygame.font.Font(self.font, 16).render(self.text, True, Color("WHITE"))

    def update(self):
        self.caret_timer -= 1
        if self.caret_timer == 0:
            self.caret_timer = self.tick_time
            self.caret_visible = not self.caret_visible

        if self.active:
            self.txt_surface = pygame.font.Font(self.font, 16).render(self.text, True, Color("WHITE"))
        else:
            self.txt_surface = pygame.font.Font(self.font, 16).render(self.text, True, Color("BLACK"))

    def show(self, screen):
        # Draw the text
        screen.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + 6))
        # Draw the rect
        pygame.draw.rect(screen, self.color, self.rect, 2)

        if self.caret_visible and len(self.text) > 0 and self.active:
            temp_text = pygame.font.Font(self.font, 16).render(self.text[:self.caret_position], True, Color("WHITE"))
            x_offset = 10 + temp_text.get_width()
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x + x_offset, self.y + 6, 2, 20))
